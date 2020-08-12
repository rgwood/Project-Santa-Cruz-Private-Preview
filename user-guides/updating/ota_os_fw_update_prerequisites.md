# OTA OS and FW Update Prerequisites

1. Toggle Azure Device Update (ADU) on. This can be accomplished through the [onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) process or in your [Azure account](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) after onboarding has been completed. After turning on ADU, please wait 5 business days for the service to propagate to your Azure account. 

    ![onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_dps_adu.png)

1. Add the ADU service principal within your AAD tenant. Launch PowerShell and run the following commands with Azure AD Admin permissions:

    1. "Install-Module AzureAD" (if you don’t already have this Powershell Module)
    
    1. "Connect-AzureAD"
    
    1. "New-AzureADServicePrincipal -AppId '6ee392c4-d339-4083-b04d-6b7947c6cf78'"

1. Assign ADU roles to users who will be performing ADU OTA updates. Currently, ADU supports FullAccessAdmin and ReadOnlyAdmin. To assign ADU roles for users, do the following:

    1. Sign in to the Azure portal.
    
    1. Select Azure Active Directory.
    
    1. Select Enterprise applications.
    
    1. On the Enterprise applications - All applications pane, change the Application Type to 'Microsoft Applications' and click Apply.
    
    1. Search for the Azure Device Update application by name or by ID (application ID: 6ee392c4-d339-4083-b04d-6b7947c6cf78). Select Azure Device Update.
    
    1. On the Azure Device Update pane, select 'Users & Groups'.
    
    1. On the Azure Device Update 'User & Groups' pane, select 'Add user'.
    
    1. On the 'Add Assignment' pane, select a user or a group.
    
    1. On the 'Add Assignment' pane, select Role and add either 'Allow full access to ADU management APIs' or 'Allow read-only access to ADU management APIs'.
    
    1. Select the 'Assign' button at the bottom of the pane.

