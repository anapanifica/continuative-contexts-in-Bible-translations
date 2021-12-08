# Continuative contexts in the Gospel of Luke

This repository contains scripts used in my paper "К описанию релевантных контекстов для континуатива (Евангелие от Луки)" (in prep.).

`what_langs_have_Luke_translations.py` takes a list of all files with translations in the parallel Bible corpus, selects translations into languages which are included in my database and then selects only those translations which contain the translation of the Gospel of Luke. The results are saved to `bible_to_analyze.txt`.

Then I manually select the version of the translation for each language (if there are more than one) and put the name of the file to the column `Bible` in the current version of `sample.csv`.

`find_contexts_with_continuative_markers.Rmd` contains a description of the rest of the process: it takes continuative markers, creates a set of commands which search for the continuative markers in the translations (then you need to run these commands from the command line), runs the script `select_numbers_of_verses_with_continuatives_in_Luke.py` which selects only those occurences of continuative markers which belong to Luke and, finally, it checks the occurences of the continuative markers in the continuative contexts.