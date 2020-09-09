# OTA OS and FW Update Prerequisites

1. Toggle Azure Device Update (ADU) on. This can be accomplished through the [onboarding website](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md). After turning on ADU, please wait 5 business days for the service to propagate to your Azure account.

    ![onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_dps_adu.png)

1. Add the ADU service principal within your Azure Active Directory (AAD) tenant.

    1. Launch [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7). If you do not have PowerShell, download and install the appropriate [release](https://github.com/PowerShell/PowerShell/releases).

    1. Open PowerShell and run the following commands with AAD admin permissions (if you do not have AAD admin permissions, please contact your organization's admin before proceeding):

        1. ```powershell
            Install-Module AzureAD
            ```

            Enter **Y** when prompted to start the module installation.

            ![install_module](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_install_module.png)

        1. ```powershell
            Connect-AzureAD
            ```

            Enter your login details in the **Sign in** window.

            ![account_sign_in](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_account_sign_in.png)

            After you sign in, you will see your account information displayed in the PowerShell terminal confirming connection to your Azure Active Directory.

            ![connect_azuread](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_connect_azuread.png)

        1. ```powershell
            New-AzureADServicePrincipal -AppId '6ee392c4-d339-4083-b04d-6b7947c6cf78'
            ```

            You may close PowerShell after adding the ADU service principal within your AAD tenant.

1. Assign ADU roles to users who will be performing ADU OTA updates. Currently, ADU supports FullAccessAdmin and ReadOnlyAdmin. To assign ADU roles for users, do the following:

    1. Sign in to the [Azure portal](https://portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod).

    1. Select **Azure Active Directory**. Use the search bar if the Azure Active Directory icon is not present on your portal homepage.

        ![azure_portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_azure_portal.png)

    1. Select **Enterprise applications** on the left pane.

        ![azure_active_directory](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_azure_active_directory.png)

    1. On the **Enterprise applications | All applications** page, change the **Application type** to **Microsoft Applications** and click **Apply**.

        ![enterprise_applications](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_enterprise_applications.png)

    1. In the search bar, type Azure Device Update or its application ID (application ID: 6ee392c4-d339-4083-b04d-6b7947c6cf78). Select **Azure Device Update**.

        ![all_applications](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_all_applications.png)

    1. On the **Azure Device Update** page, select **Users and groups**.

        ![azure_device_update](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/prereqs_azure_device_update.png)

    1. On the **Azure Device Update | Users and groups** page, select **Add user**.

    1. On the **Add Assignment** page, select a user or a group.

    1. On the **Add Assignment** page, select **Role** and add either **Allow full access to ADU management APIs** or **Allow read-only access to ADU management APIs**.

    1. Select the **Assign** button at the bottom of the page.

## Next steps

Once you have completed the steps above, you will be able to use Azure Device Update by navigating to the [Azure Portal](https://portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod). This link turns on Azure Device Update functionality, which is a Private Preview feature.

The first time you use Azure Device Update, you will be asked to provide your Azure Device Update Account name and Instance name. Your Account name and Instance name are located on the [onboarding website](https://aka.ms/projectsantacruz) under the Azure Device Update section.

You are now ready to deploy your first OS/FW update over-the-air. Check out the [OTA carrier board OS update walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ota_update.md) and the [OTA Ear SoM FW update walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ear_som_firmware.md) to learn more.
