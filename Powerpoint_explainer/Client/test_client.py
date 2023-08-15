from Powerpoint_explainer.Client.client import WebAPIClient

if __name__ == '__main__':
    client = WebAPIClient()

    # Upload a sample PowerPoint file
    uid = client.upload_file('path_to_your_sample.pptx')
    print(f'Upload successful. UID: {uid}')

    # Check the status of the upload
    status = client.get_status(uid)
    print(f'Status: {status}')
