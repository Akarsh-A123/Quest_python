*** Settings ***
Library   SeleniumLibrary
Library   Collections
*** Variables ***
${from}    Coimbatore
${to}      Trivandrum
*** Test Cases ***
TC-001 Verify if a user is able to filter bus according to their seat preference
    Open Make My trip AS
    search busses   ${from}  ${to}
    Select Filter     AC     AC
    Get All Bus Id
    
*** Keywords ***
Open Make My trip AS
    Open Browser  browser=chrome
    Go To  url=https://www.makemytrip.com
    Maximize Browser Window
    Wait Until Element Is Visible  //span[@data-cy="closeModal"]
    Click Element   //span[@data-cy="closeModal"]

search busses
    [Arguments]    ${fromcity}    ${tocity}
    Click Element  //nav//li[contains(@class,'menu_Buses')]

    Wait Until Element Is Visible   fromCity
    Click Element   fromCity
    Wait Until Element Is Visible  //input[@placeholder="From"]  10s
    Input Text  //input[@placeholder="From"]  ${fromcity}
    Wait Until Element Is Visible  //div[contains(@class,'autosuggest')]//span[contains(text(),'${fromcity},')]
    Click Element    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${fromCity},')]


    Wait Until Element Is Visible     toCity     10s
    Run Keyword And Ignore Error        Click Element        toCity
    Wait Until Element Is Visible     //input[@placeholder="To"]     10s
    Input Text       //input[@placeholder="To"]     ${toCity}
    Wait Until Element Is Visible       //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]
    Click Element    //div[contains(@class, 'autosuggest')]//span[contains(text(),'${toCity},') or contains(text(),'(${toCity}),')]

    Run Keyword And Ignore Error  Click Element    travelDate
    Wait Until Element Is Visible     //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[text()='19']   10s
    Click Element    //div[contains(text(), 'August')]/ancestor::div[@class="DayPicker-Month"]//div[text()='19']
    Click Element    search_button
    Wait Until Element Is Visible     //div[@class="busListingContainer"]//p[contains(text(),'found')]


    

Select Filter
    [Arguments]     ${filterType}     ${filterExactText}
    # take the initial count
    Click Element     toggle_buses
    ${initialCount}    Get Element Count     //div[@class="busCardContainer "]     # maximum bus in search result, no filter applied
    Click Element    //div[contains(text(),'${filterType}')]/../..//span[text()='${filterExactText}']
    Wait Until Element Is Not Visible     //div[@class="busListingContainer"]//p[contains(text(),'found') and contains(text(),'${initialCount}')]
    #wait till its not the previous count or wait till elemnt disappears.

Get All Bus Id

    @{allACBus}    Create List
    run keyword and ignore error     Click Element     //div[@id="toggle_buses" and not(contains(@class,'active'))]
    ${numberOfBuses}     Get Element Count    //div[contains(@class,'busCardContainer')]//p[not(contains(text(),'Non A/C')) and contains(text(),'A/C')]
    ${numberOfBuses}    Evaluate     $numberOfBuses+1
    FOR    ${index}    IN RANGE     1    ${numberOfBuses}
    ${busId}     Get Text  (//div[contains(@class,'busCardContainer')]//p[not(contains(text(),'Non A/C')) and contains(text(),'A/C')])[${index}]         # node with id in it, exact 16 matches.
    Append To List    ${allACBus}    ${busId}
    

    END
    ${count}  Get Count   ${allACBus}  AC
    Log    ${allACBus}
    Log    ${count}