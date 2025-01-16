class MyConfig:

    def __init__(self, ftp_host=None, ftp_username=None, ftp_password=None,
                 sharepoint_url=None, sharepoint_clientid=None, sharepoint_clientsecret=None, azure=False):

        self._ftp_host = ftp_host
        self._ftp_username = ftp_username
        self._ftp_password = ftp_password
        self._sharepoint_url = sharepoint_url
        self._sharepoint_clientid = sharepoint_clientid
        self._sharepoint_clientsecret = sharepoint_clientsecret