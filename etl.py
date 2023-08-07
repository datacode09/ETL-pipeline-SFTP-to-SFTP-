import paramiko
import logging
import os

# Configure logging
logging.basicConfig(filename='pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    source_sftp_host = 'source_server_host'
    source_sftp_port = 22
    source_sftp_username = 'source_username'
    source_sftp_password = 'source_password'
    source_sftp_path = '/path/to/source/file.txt'

    dest_sftp_host = 'dest_server_host'
    dest_sftp_port = 22
    dest_sftp_username = 'dest_username'
    dest_sftp_password = 'dest_password'
    dest_sftp_path = '/path/to/destination/'

    try:
        # Connect to source SFTP server
        source_transport = paramiko.Transport((source_sftp_host, source_sftp_port))
        source_transport.connect(username=source_sftp_username, password=source_sftp_password)
        source_sftp = paramiko.SFTPClient.from_transport(source_transport)

        # Download file from source SFTP
        local_filename = os.path.basename(source_sftp_path)
        local_path = os.path.join('downloaded_files', local_filename)
        source_sftp.get(source_sftp_path, local_path)

        # Disconnect from source SFTP server
        source_sftp.close()
        source_transport.close()

        # Connect to destination SFTP server
        dest_transport = paramiko.Transport((dest_sftp_host, dest_sftp_port))
        dest_transport.connect(username=dest_sftp_username, password=dest_sftp_password)
        dest_sftp = paramiko.SFTPClient.from_transport(dest_transport)

        # Upload file to destination SFTP
        dest_sftp.put(local_path, os.path.join(dest_sftp_path, local_filename))

        # Disconnect from destination SFTP server
        dest_sftp.close()
        dest_transport.close()

        # Log success
        logging.info(f"File '{local_filename}' transferred successfully from source to destination.")

    except Exception as e:
        # Log error
        logging.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
