import os
from unittest import TestCase, main
import shutil
from BibCleaner import cleandict


class TestCleandict(TestCase):
    def test_cleandict(self):
        """ Test removal with template files
        :return: none
        """
        original_file = "test_files/My Collection.bib"
        test_file = "test_files/My Collection2.bib"
        new_file = "test_files/new_file.bib"
        shutil.copyfile(original_file, new_file)
        cleandict(new_file, customdict={'year': 1, 'abstract': 1, 'file': 1})
        with open(test_file, 'r', encoding='utf-8') as f1, open(new_file, 'r', encoding='utf-8') as f2:
            for line in f1:
                self.assertTrue(f2.readline() == line, msg="Files are not equal for line"+line)
        os.remove(new_file)


if __name__ == '__main__':
    main()