DoesIsLibrary for Robot Framework
==================================================


Introduction
------------

RobotFramework library which extends imported libraries with *Does* and *Is* keywords.

RobotFramework libraries provides assertion keywords, usually named like *Something Should Exist*, *Another Thing Should Be Eqal*, *Yet Another Should Not Exist*, *Some Should Not Be Equal*. This library extracts such keywords from libraries imported in suite, and extends libraries from where those keywords come from with *Does* and *Is* keywords, like:

Orginal keyword - Newly created keyword
*Something Should Exist* - *Does Somethin Exist*
*Another Thing Should Be Eqal* - *Is Another Thing Equal*
*Yet Another Should Not Exist* - *Does Yest Another Not Exist*
*Some Should Not Be Equal* - *Is Some Not Equal*


Orginal Keywords PASS or FAIL depending of assertion is met or not, while newly created keyword returns `True` or `False`
Use Case is shown in follwing example:

Usage
-----

WithoutLibrary.robot

    *** Settings ***
    Library      SeleniumLibrary

    *** Test Cases ***
    NoLibrary
        ${are_equal}=        Run Keyword And Return Status      Should Be Equal As Numbers     10     10
        Run Keyword If    '${are_equal}'=='True'     Log     Equal!
        Open Browser      http://example.local     gc
        ${is_element_visible}=        Run Keyword And Return Status      Element Should Be Visible    id=locator
        Run Keyword If    '${is_element_visible}'=='True'     Click Element   id=locator

WithLibrary.robot

    *** Settings ***
    Library      SeleniumLibrary
    Library      DoesIsLibrary

    *** Test Cases ***
    WithLibrary
        ${are_equal}=         Is Equal As Numbers     10     10
        Run Keyword If    '${are_equal}'=='True'     Log     Equal!
        Open Browser      http://example.local     gc
        ${is_element_visible}=        Is Element Visible    id=locator
        Run Keyword If    '${is_element_visible}'=='True'     Click Element   id=locator


Library Does not provide almost all "static" keywords, except `List Is Keywords` and `List Does keywords` which place names of newly dynamically generated keywords in RF log.html file.

- Information about keywords can be found on the [Keyword Documentation](https://raw.githack.com/sebastianciupinski/robotframework-doesislibrary/master/docs/DoesIsLibrary.html) page.

How it works and limitations
----------------------------

Library is looking for imported libraries from ***Settings*** section during start suite phase and then looks for keyword having 'should' in keyword name. Then new keywords are created for each imported library respectively.
As (for now) new keyword generation is triggerd in suite setup phase, new keywords *will not be generated* for libraries imported with RF built in keyword `Import Library`


Requirements
------------
* Robot Framework


Installation
------------
#### Using pip ####

The recommended installation tool is [pip](http://pip-installer.org).

Install pip.
Enter the following:

    pip install robotframework-doesislibrary





