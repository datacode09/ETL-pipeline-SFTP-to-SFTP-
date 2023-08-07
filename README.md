# ETL-pipeline-SFTP-to-SFTP
This script uses the paramiko library to interact with SFTP servers. You should install it using pip install paramiko.

Here are some important points to consider:

Replace placeholders (source_server_host, source_username, etc.) with actual values.
Ensure you have the necessary permissions and access credentials for both SFTP servers.
Modify the file paths and directories as needed.
Customize error-handling to fit your requirements.
This example doesn't cover advanced error handling, monitoring, or optimizations.

First, install the necessary packages if you haven't already:

bash
Copy code
pip install paramiko coverage
Create a file named test_pipeline.py for unit testing:

```
import unittest
import paramiko
import os
from unittest.mock import patch
from pipeline import main

class TestPipeline(unittest.TestCase):

    @patch('pipeline.paramiko.Transport')
    @patch('pipeline.paramiko.SFTPClient.from_transport')
    def test_successful_file_transfer(self, mock_sftp_from_transport, mock_transport):
        mock_sftp = mock_sftp_from_transport.return_value
        mock_transport_instance = mock_transport.return_value

        mock_sftp_path = '/path/to/source/file.txt'
        local_filename = os.path.basename(mock_sftp_path)
        local_path = os.path.join('downloaded_files', local_filename)

        main()

        mock_transport.assert_called_with(('source_server_host', 22))
        mock_transport_instance.connect.assert_called_with(username='source_username', password='source_password')
        mock_sftp_from_transport.assert_called_with(mock_transport_instance)
        mock_sftp.get.assert_called_with(mock_sftp_path, local_path)

        mock_transport.assert_called_with(('dest_server_host', 22))
        mock_transport_instance.connect.assert_called_with(username='dest_username', password='dest_password')
        mock_sftp_from_transport.assert_called_with(mock_transport_instance)
        mock_sftp.put.assert_called_with(local_path, os.path.join('/path/to/destination/', local_filename))

if __name__ == '__main__':
    unittest.main()
```
Run the unit tests:
```
python -m unittest test_pipeline.py
```
Create a file named .coveragerc to configure the coverage tool:
```
[run]
source = .
omit = */venv/*

[report]
show_missing = true
```
Run coverage tests:
```
coverage run --source=. -m unittest test_pipeline.py
```
Generate coverage report:
```
coverage report
```
This will provide you with a coverage report showing how much of your code is covered by tests.

Please note that this example focuses on unit tests and basic coverage tests. For a more comprehensive testing strategy, you might want to consider additional test cases, integration tests, and more advanced error scenarios. Also, remember to adapt the test code according to any changes you make in your main pipeline script.
