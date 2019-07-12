"""
Utility functions for processing JUnit XML reports and
Cobertura coverage XML reports into Markdown
"""

from .process_cobertura import (get_coverage_from_cobertura_xml,
                                process_cobertura_xml)
from .process_junit import process_junit_xml

__all__ = [
    'process_junit_xml', 'process_cobertura_xml',
    'get_coverage_from_cobertura_xml',
]
