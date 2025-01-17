import os
import subprocess
import win32security
import win32api
import win32con

class SecureAccess:
    def __init__(self):
        self.users = self.get_users()

    def get_users(self):
        users = []
        try:
            local_users = subprocess.check_output('net user', shell=True).decode().split('\n')
            for user_line in local_users:
                if user_line.strip() and not user_line.startswith('----'):
                    users.extend(user_line.split())
            return users
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving users: {e}")
            return []

    def set_user_permission(self, username, folder_path, permission):
        try:
            if username not in self.users:
                print(f"User {username} does not exist.")
                return

            sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)
            dacl = sd.GetSecurityDescriptorDacl()

            user_sid, _, _ = win32security.LookupAccountName(None, username)
            permission_flags = self.get_permission_flags(permission)

            dacl.AddAccessAllowedAce(win32security.ACL_REVISION, permission_flags, user_sid)
            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)

            print(f"Permissions {permission} set for user {username} on {folder_path}.")
        except Exception as e:
            print(f"Error setting permissions: {e}")

    def get_permission_flags(self, permission):
        permission_map = {
            'read': win32con.FILE_GENERIC_READ,
            'write': win32con.FILE_GENERIC_WRITE,
            'full': win32con.FILE_ALL_ACCESS
        }
        return permission_map.get(permission, 0)

    def display_permissions(self, folder_path):
        try:
            sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)
            dacl = sd.GetSecurityDescriptorDacl()
            for i in range(dacl.GetAceCount()):
                ace = dacl.GetAce(i)
                sid = ace[2]
                user, _, _ = win32security.LookupAccountSid(None, sid)
                access_mask = ace[1]
                print(f"User: {user}, Access: {self.decode_access_mask(access_mask)}")
        except Exception as e:
            print(f"Error displaying permissions: {e}")

    def decode_access_mask(self, access_mask):
        if access_mask == win32con.FILE_GENERIC_READ:
            return "Read"
        elif access_mask == win32con.FILE_GENERIC_WRITE:
            return "Write"
        elif access_mask == win32con.FILE_ALL_ACCESS:
            return "Full"
        return "Unknown"

if __name__ == "__main__":
    sa = SecureAccess()
    print("Available users:", sa.users)
    folder = r"C:\Path\To\Your\Folder"
    sa.set_user_permission("username", folder, "read")
    sa.display_permissions(folder)