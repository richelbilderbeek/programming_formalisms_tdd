# programming_formalisms_small_project

[![Check links](https://github.com/richelbilderbeek/programming_formalisms_small_project/actions/workflows/check_links.yaml/badge.svg?branch=master)](https://github.com/richelbilderbeek/programming_formalisms_small_project/actions/workflows/check_links.yaml)
[![Check spelling](https://github.com/richelbilderbeek/programming_formalisms_small_project/actions/workflows/check_spelling.yaml/badge.svg?branch=master)](https://github.com/richelbilderbeek/programming_formalisms_small_project/actions/workflows/check_spelling.yaml)
[![Measure Codecov](https://github.com/richelbilderbeek/programming_formalisms_small_project/actions/workflows/measure_coverage.yml/badge.svg?branch=master)](https://github.com/richelbilderbeek/programming_formalisms_small_project/actions/workflows/measure_coverage.yml)

[The Small Project](https://github.com/UPPMAX/programming_formalisms/blob/main/learning_line.md#functions-to-be-developed-for-the-small-project) 
in [the Programming Formalisms course](https://github.com/UPPMAX/programming_formalisms).

This repo does not use a formal testing framework,
as the focus of this part of the course is to do many iterations of TDD.
In [The Medium Project](https://github.com/UPPMAX/programming_formalisms/blob/main/learning_line.md#functions-to-be-developed-for-the-medium-project)
there will be a formal testing framework.

## Files

Filename                            |Descriptions
------------------------------------|------------------------------------------------------------------------------------------------------
[mlc_config.json](mlc_config.json)  |Configuration of the link checker
[.spellcheck.yaml](.spellcheck.yaml)|Configuration of the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally
[.wordlist.txt](.wordlist.txt)      |Whitelisted wordss for the spell checker, use `pyspelling -c .spellcheck.yml` to do spellcheck locally

