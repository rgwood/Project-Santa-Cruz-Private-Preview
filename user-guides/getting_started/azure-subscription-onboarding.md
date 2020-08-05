<!---
title: Project Santa Cruz onboarding                     # the article title to show on the browser tab
description: Walks a user through the onboarding process for Project Santa Cruz Private Preview (July 2020). 
author: elqu20      # the author's GitHub ID - will be auto-populated if set in settings.json
ms.author: v-elqu     # the author's Microsoft alias (if applicable) - will be auto-populated if set in settings.json
ms.date: {@date}           # the date - will be auto-populated when template is first applied
ms.topic: reference  # the type of article
--->
# Project Santa Cruz onboarding

Welcome to Project Santa Cruz! Prior to getting started with Santa Cruz devkits and devices, please complete the onboarding as described herein. The onboarding process involves connecting an appropriate Azure subscription and IoT Hub to Project Santa Cruz, which allows you to connect, manage, and update your devices with ease. Perform the following steps to complete the onboarding:

1. Read and sign the Project Santa Cruz NDA and provide your tenant ID through the Private Preview email invitation. If you have not received an email invitation, please reach out to your Project Santa Cruz representative for assistance.
    1. To locate your tenant ID, sign in to the [Azure Portal](https://ms.portal.azure.com/#home) and click View under Manage Azure Active Directory. If this link is not available on your portal’s home screen, type Azure Active Directory into the search bar at the top of the page and click on the link with the blue pyramid icon.

        ![azure_portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_azure_portal.png)

    1. The tenant ID will be displayed in the Tenant information box on the Overview page of Azure Active Directory. For more information on tenant IDs, please view the Azure Active Directory [documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant). 

        ![azure_active_directory](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_azure_active_directory.png)

    1. You will be able to access the Project Santa Cruz onboarding website within three to four days of submitting your Private Preview agreement.
 
1. Once your Private Preview agreement has been processed, open a browser and enter aka.ms/projectsantacruz in the address bar to access the onboarding tool.  

1. Enter your account login details and click Next. The account must be associated with the tenant ID provided through the Private Preview email invitation.  
 
    ![onboarding_welcome_page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_welcome_page.png)

1. Click Get Started on the onboarding welcome screen. 

    ![onboarding_get_started](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_get_started.png)

1. Select the Azure subscription you would like to use with Project Santa Cruz from the drop-down menu. If you do not have an Azure subscription, or if you would like to create a new subscription to use with Project Santa Cruz, click Learn more. This link redirects to the Azure website where you may create a new Azure account. Note that the free account, which currently provides $200 in credits to use within 30 days of the account opening, is sufficient to get started with Project Santa Cruz. Your account credit card will be charged for usage following the exhaustion or expiration of the credits. After you have selected the appropriate Azure subscription from the drop-down on the onboarding screen, click Next. 

    ![onboarding_select_azure_subscription](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_select_azure_subscription.png)

1. Create an IoT Hub.  

    1. Enter your IoT Hub name. It is recommended that you create a new IoT Hub for working solely with Project Santa Cruz.  

    1. Select your hub’s pricing tier from the drop-down menu. The S1 tier is recommended for use with Project Santa Cruz as the F1 tier has limited messaging capacity and cannot be upgraded. Other pricing tiers do not support IoT Edge, which is required. Note that Azure account credits may be used towards IoT Hub fees.   

    1. Select a resource group from the drop-down menu or create a new one.  

    1. Select your location from the drop-down menu. Note that you may use any available region regardless of your country of residence.  

    1. After selecting your IoT Hub properties, click Submit. After submitting, any changes to your IoT properties can be made in your [Azure account](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home). 
    
    ![onboarding_create_iot_hub](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_create_iot_hub.png)
    
1. Toggle Device Provisioning Service (DPS) to the ON position and enter your DPS name.  

1. Toggle Azure Device Update (ADU) and Automatic Import Updates to the ON Position. Click Submit. After submitting, any changes to these properties can be made in your [Azure account](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) (this link allows you to access the Azure Device Update extension, which is a Private Preview service).

    ![onboarding_dps_adu](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_dps_adu.png)  

1. After submitting, you will receive a confirmation page with settings summary. 

    ![onboarding_confirmation](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_confirmation.png) 

Congratulations! You have successfully completed the onboarding tool and are ready to get started with Project Santa Cruz. As a reminder, any changes to the settings you selected in the onboarding tool can now be made in your Azure account.  

## Next steps

Once you have received a Project Santa Cruz Development Kit, please see the [unboxing guide](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md) for information on powering on your device and accessing the [OOBE (out of box experience)](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md).  