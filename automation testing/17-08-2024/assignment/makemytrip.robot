*** Settings ***
Library   SeleniumLibrary
Library    Collections
*** Variables ***
${from}  coimbatore
${to}    trivandram
*** Test Cases ***
TC-001 Verify if a user is able to filter bus according to their seat preference
   Open make my trip
   Search bus    Coimbatore   Trivandrum
   Select filter  AC  AC
   Get bus id
*** Keywords ***
open make my trip 
    Open Browser  browser=chrome
    Go To  url=https://www.makemytrip.com
    Maximize Browser Window
    Wait Until Element Is Visible  //span[@class='commonModal__close']  10s
    Click Element    //span[@class='commonModal__close']
Search bus
    [Arguments]   ${fromcity}   ${tocity}
    Click Element  //li[@class='menu_Buses']
    Wait Until Element Is Visible   fromCity      10s
    Click Element    fromCity
    Wait Until Element Is Visible  //input[contains(@placeholder,'From')]
    Input Text   //input[contains(@placeholder,'From')]  ${fromcity}
    Wait Until Element Is Visible  //div[contains(@class,'autosuggest')]//span[contains(text(),'${fromcity},')]
    Click Element  //div[contains(@class,'autosuggest')]//span[contains(text(),'${fromcity},')]

    Run Keyword And Ignore Error  Click Element    toCity
    Wait Until Element Is Visible  //input[contains(@placeholder,'To')]
    Input Text   //input[contains(@placeholder,'To')]  ${tocity}
    Wait Until Element Is Visible  //div[contains(@class,'autosuggest')]//span[contains(text(),'(${tocity})')]
    Click Element  //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]

    Run Keyword And Ignore Error  Click Element    travelDate
    Wait Until Element Is Visible  //div[contains(text(),'August')]/ancestor::div[@class='DayPicker-Month']//div[contains(text(),'20') and @class='DayPicker-Day']
    Click Element   //div[contains(text(),'August')]/ancestor::div[@class='DayPicker-Month']//div[contains(text(),'20') and @class='DayPicker-Day']
    Click Element   search_button
    Wait Until Element Is Visible     //div[@class="busListingContainer"]//p[contains(text(),'found')]

Select filter
    [Arguments]     ${filterType}     ${filterExactText}
    Click Element  toggle_buses
    ${initialcount}  Get Element Count   //div[@class="busCardContainer "] 
    Click Element  //div[contains(text(),'${filterType}')]/../..//span[contains(text(),'${filterExactText}')]
    Wait Until Page Does Not Contain   //p[contains(text(),'found') or contains(text(),'${initialcount}')]

Get bus id
    @{allACBus}  Create List
    Run Keyword And Ignore Error  Click element  //div[@id="toggle_buses" and not(contains(@class,'active'))]
    ${numberofbusses}  Get Element Count  //div[contains(@class,'busCardContainer')]
    ${numberofbusses}  Evaluate  $numberofbusses+1
    FOR  ${index}  IN RANGE  1  ${numberofbusses}
    ${ACBus}   Get Text  (//div[contains(@class,'busCardContainer')]//p[contains(@class,'secondaryTxt')])[${index}]
    Log  ${ACBus}
    Append To List  ${allACBus}   ${ACBus}

    
    END
    Log   ${allACBus}
    List Should Not Contain Value   ${allACBus}  Non AC

    





