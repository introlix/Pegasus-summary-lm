import os

class GCloudSync:
    
    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        """
        Function to sync files from local machine to Google Cloud Storage
        
        Args:
            gcp_bucket_url (str): Google Cloud Storage bucket URL
            filepath (str): Local file path
            filename (str): Local file name

        """

        command = f"gsutil cp {filename}/{filepath} gs://{gcp_bucket_url}"

        os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):

        """
        Function to sync the folder from the gclooud to local machine

        Args:
            gcp_bucket_url (str): Google Cloud Storage bucket URL
            filename (str): Local file name
            destination (str): Local file path
        """

        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"

        os.system(command)