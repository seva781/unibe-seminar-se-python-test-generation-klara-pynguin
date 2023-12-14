"""A test generator using Klara."""

import re

import klara.contract.__main__ as klara_main

from python_tool_competition_2024.generation_results import (
    FailureReason,
    TestGenerationFailure,
    TestGenerationResult,
    TestGenerationSuccess,
)
from python_tool_competition_2024.generators import FileInfo, TestGenerator


class KlaraTestGenerator(TestGenerator):
    """A test generator using Klara."""

    def build_test(self, target_file_info: FileInfo) -> TestGenerationResult:
        """
        Genereate a test for the specific target file.

        Args:
            target_file: The `FileInfo` of the file to generate a test for.

        Returns:
            Either a `TestGenerationSuccess` if it was successful, or a
            `TestGenerationFailure` otherwise.
        """
        target_body = target_file_info.absolute_path.read_text()
        target_module_name = target_file_info.module_name
        try:
            test_body = klara_main.run(target_body, target_module_name)
        except NotImplementedError as error:
            error_str = str(error)
            if error_str.startswith("Type other than ") and error_str.endswith(
                " is not supported yet!"
            ):
                return TestGenerationFailure(
                    (error_str,), FailureReason.UNSUPPORTED_FEATURE_USED
                )
            raise
        except AttributeError as error:
            match = _INVALID_ATTRIBUTE_REGEX.match(str(error))
            if match:
                return _unsupported_feature_result(match.group("object_name"))
            raise
        except SyntaxError as error:
            if error.text and ":=" in error.text:
                return _unsupported_feature_result(":=")
            raise

        if _is_empty_result(test_body, target_module_name):
            return TestGenerationFailure(
                (
                    "Klara did generate nothing.",
                    "Maybe there are no functions, no return value or only unsupported "
                    "types.",
                ),
                FailureReason.NOTHING_GENERATED,
            )

        return TestGenerationSuccess(test_body)


_INVALID_ATTRIBUTE_REGEX = re.compile(
    r"'(?P<object_name>[^']+)' object has no attribute '(?P<attribute_name>[^']+)'"
)


def _is_empty_result(test_body: str, target_module_name: str) -> bool:
    return test_body.strip() == f"import {target_module_name}"


def _unsupported_feature_result(feature: str) -> TestGenerationFailure:
    return TestGenerationFailure(
        (f"Unsupported syntax used: {feature}",),
        FailureReason.UNSUPPORTED_FEATURE_USED,
    )
