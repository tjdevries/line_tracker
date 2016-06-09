#!/usr/bin/env python3

# import pytest
# import os

from git import Repo
from line_tracker.line_tracker import (
        get_diff,
        get_diff_object,
        get_diff_text,
        get_diff_text_lines,
        debug,
        # find_diffed_line,
        # find_similar_line
    )


expected_diff_1 = [
    '@@ -1,5 +1,6 @@',
    ' This is the first commit of this file.',
    ' ',
    '-This is an example text line.',
    '+Add a line above.',
    '+This is a new example text line.',
    ' ',
    ' Other stuff is down here.'
]

expected_diff_2 = [
    '@@ -1,6 +1,10 @@',
    ' This is the first commit of this file.',
    ' ',
    '+Let\'s add a lot of lines.',
    ' Add a line above.',
    '-This is a new example text line.',
    '+This was another line added.',
    '+This is an old example text line.',
    '+This is the line below it now!',
    '+Random!!~~! :D',
    ' ',
    ' Other stuff is down here.'
]


class TestLineTracker:
    @classmethod
    def setup_class(cls):
        # TODO: Parameterize
        cls.repo = Repo('/home/tj/Git/line_tracker/')
        print(cls.repo)

        # These are actual commits and hashses from this repo
        # Test: Add file
        cls.h1 = '0847d03906abcba1b00bbe79ae7fed77f9ca78a8'

        # Test: Add more lines and modify the line
        cls.h2 = '9126e7b09dac47ed8b06a6f12f6d3683e63bd28b'

        # Test: Change line and move down one
        cls.h3 = '794ed68520edb3086a96339aa7cd18a3c618cfa0'

        cls.file_name = 'test/test_files/test_1.txt'
        cls.line_find = 'This is an example text line.'

    def test_get_diff_text_commit_1(self):
        current_diff = get_diff(self.h1, self.h2, self.repo)
        diff_obj = get_diff_object(current_diff,
                                   self.file_name,
                                   self.repo,
                                   debug)
        diff_text = get_diff_text(self.repo, diff_obj)
        diff_lines = get_diff_text_lines(diff_text)

        assert diff_lines == expected_diff_1

    def test_get_diff_text_commit_2(self):
        current_diff = get_diff(self.h2, self.h3, self.repo)
        diff_obj = get_diff_object(current_diff,
                                   self.file_name,
                                   self.repo,
                                   debug)
        diff_text = get_diff_text(self.repo, diff_obj)
        diff_lines = get_diff_text_lines(diff_text)

        assert diff_lines == expected_diff_2

"""
Old stuff:
current_diff = get_diff(h1, h2, repo)
diff_obj = get_diff_object(current_diff, file_name, repo, debug)
diff_text = get_diff_text(repo, diff_obj)
diff_lines = diff_text.split('\n')

orig_line = find_diffed_line(find, '-', diff_lines)
print('Orig Line Number: {0}\n\tOrig Line: {1}'.format(orig_line, find))

new_index = find_similar_line(find, '+', diff_lines)
new_find = diff_lines[new_index][1:]
new_line = find_diffed_line(new_find, '+', diff_lines)
print('New Line Number: {0}\n\tNew Line: {1}'.format(new_line, new_find))

example_diff = [
     "@@ -1,7 +1,5 @@",
     " #!/bin/bash",
     "-",
     "-echo 'Tracking line numbers through git history'",
     "-",
     "+echo 'Tracking line numbers through history'",
     " PARAMS=\"$*\" ",
     " LINE=$(git blame $PARAMS) ",
     " while test $? == 0 ",
     ]


class TestFindSimilarLine:
    def test_small_change(self):
        find = "echo 'Tracking line numbers through history'"

        assert(3 == find_similar_line(find, '-', example_diff))


class TestFindDiffedLine:
    def test_small_change_previous_commit(self):
        find = "echo 'Tracking line numbers through history'"

        assert(2 == find_diffed_line(find, '+', example_diff))



@pytest.mark.incremental
def setup_git_dir():
    repo_dir = os.path.join('./', 'my-new-repo')
    file_name = os.path.join(repo_dir, 'new-file')

    r = Repo.init(repo_dir)
    # This function just creates an empty file ...
    open(file_name, 'wb').close()
    r.index.add([file_name])
    r.index.commit("initial commit")


def teardown_git_dir():
    pass
"""
