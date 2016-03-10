from unittest import TestCase
from test.plugins.ReqTracer import requirements
import source.git_utils
import mock
import os
from source.main import Interface


# pylint: disable=C0111

class TestGitUtils(TestCase):
    # get_git_file_info
    @requirements(['#0101'])
    @mock.patch('source.git_utils.get_diff_files')
    def test_status_get_diff_files(self, mock_get_diff_files):
        mock_get_diff_files.return_value = os.path.abspath(__file__)
        result = source.git_utils.get_git_file_info(__file__)
        self.assertEqual(result, os.path.basename(__file__) + ' has been modified locally')

    @requirements(['#0101'])
    @mock.patch('source.git_utils.get_untracked_files')
    @mock.patch('source.git_utils.get_diff_files')
    def test_status_get_untracked_files(self, mock_get_diff_files, mock_get_untracked_files):
        mock_get_diff_files.return_value = []
        mock_get_untracked_files.return_value = os.path.abspath(__file__)
        result = source.git_utils.get_git_file_info(os.path.relpath(__file__))
        self.assertEqual(result, os.path.basename(__file__) + ' has been not been checked in')

    @requirements(['#0101'])
    @mock.patch('source.git_utils.is_repo_dirty')
    @mock.patch('source.git_utils.get_untracked_files')
    @mock.patch('source.git_utils.get_diff_files')
    def test_status_is_repo_dirty(self,
                                  mock_get_diff_files,
                                  mock_get_untracked_files,
                                  mock_is_repo_dirty):
        mock_get_diff_files.return_value = []
        mock_get_untracked_files.return_value = []
        mock_is_repo_dirty = os.path.abspath(__file__)
        result = source.git_utils.get_git_file_info(__file__)
        self.assertEqual(result, os.path.basename(__file__) + ' is a dirty repo')

    @requirements(['#0101'])
    @mock.patch('source.git_utils.is_repo_dirty')
    @mock.patch('source.git_utils.get_untracked_files')
    @mock.patch('source.git_utils.get_diff_files')
    def test_status_is_clear(self,
                             mock_get_diff_files,
                             mock_get_untracked_files,
                             mock_is_repo_dirty):
        mock_get_diff_files.return_value = []
        mock_get_untracked_files.return_value = []
        mock_is_repo_dirty.return_value = []
        result = source.git_utils.get_git_file_info(__file__)
        self.assertEqual(result, os.path.basename(__file__) + ' is up to date')

    @requirements(['#0101'])
    @mock.patch('source.git_utils.get_untracked_files')
    def test_status_has_untracked_files(self, mock_get_untracked_files):
        mock_get_untracked_files.return_value = os.path.abspath(__file__)
        result = source.git_utils.has_untracked_files(__file__)
        self.assertEqual(result, True)

    @requirements(['#0100'])
    @mock.patch('source.git_utils.get_diff_files')
    def test_is_file_in_repo(self, mock_get_diff_files):
        mock_get_diff_files.return_value = os.path.abspath(__file__)
        result = source.git_utils.is_file_in_repo(__name__)
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_untracked(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': [('', 'empty'), ('', 'empty'), ('git_utils_test.py', 'onlyFile'),
                                             (__file__, '4'), ('something', '5'), ('maybe', '6')]}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(os.path.relpath(__file__))
        self.assertEqual(result, 'Yes')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_subprocess_dummy_data(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info(__file__)
        self.assertEqual(result, os.path.basename(__file__) + " is a dirty repo")

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_subprocess_empty(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {' ', 'empty'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info(__file__)
        self.assertEqual(result, os.path.basename(__file__) + " is up to date")

    @requirements(['#0101'])
    @mock.patch('source.git_utils.git_execute')
    def test_func_use_git_execute(self, mock_git_execute):
        mock_git_execute.return_value = os.path.abspath(__file__)
        result = source.git_utils.get_file_info(__file__)
        self.assertEqual(result, __file__)
        result = source.git_utils.get_repo_branch(__file__)
        self.assertEqual(result, __file__)
        result = source.git_utils.get_repo_url(__file__)
        self.assertEqual(result, __file__)

    @requirements(['#0101'])
    @mock.patch('source.git_utils.git_execute')
    @mock.patch('os.path.exists')
    def test_get_repo_root(self, mock_os_path_exists, mock_git_execute):
        mock_os_path_exists.return_value = True
        mock_git_execute.return_value = os.path.abspath(__file__)
        result = source.git_utils.get_repo_root(__file__)
        self.assertEqual(result, __file__)

    @requirements(['#0100'])
    @mock.patch('source.git_utils.git_execute')
    @mock.patch('os.path.exists')
    def test_is_file_in_repo_path_exists(self, mock_os_path_exists, mock_git_execute):
        mock_os_path_exists.return_value = True
        mock_git_execute.return_value = os.path.abspath(__file__)
        result = source.git_utils.is_file_in_repo(__file__)
        self.assertEqual(result, 'No')

    @requirements(['#0101'])
    def test_path_checker(self):
        self.assertRaisesRegexp(Exception, 'Path huh does not exist cannot get git file',
                                source.git_utils.get_git_file_info, "huh")

    @requirements(['#0102'])
    @mock.patch('subprocess.Popen')
    def test_what_is_status_of_repo_hashes(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'#AO56QU, 1/2/2016, HatimP', 'error'}}
        process_mock.configure_mock(**attrs)
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(
            'What is the deal with <{}>?'.format(__file__))
        self.assertEqual(result, '#AO56QU, 1/2/2016, HatimP')

    @requirements(['#0103'])
    @mock.patch('subprocess.Popen')
    def test_what_is_branch_name(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(
            'What branch is <{}>?'.format(__file__))
        self.assertEqual(result, 'master')

    @requirements(['#0104'])
    @mock.patch('subprocess.Popen')
    def test_what_is_repo_url(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(
            'Where did <{}> come from?'.format(__file__))
        self.assertEqual(result, 'master')


