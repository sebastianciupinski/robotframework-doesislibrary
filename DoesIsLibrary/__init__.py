#!/usr/bin/env python


from .kwgenerator import DoesIsListener

class DoesIsLibrary(DoesIsListener):
    """
    DoesIsLibrary for Robot Framework :)


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

|    ***** Settings *****
|    Library      SeleniumLibrary
|
|    ***** Test Cases *****
|    NoLibrary
|        ${are_equal}=        Run Keyword And Return Status      Should Be Equal As Numbers     10     10
|        Run Keyword If       '${are_equal}'=='True'     Log     Equal!
|        Open Browser         http://example.local     gc
|        ${is_element_visible}=        Run Keyword And Return Status      Element Should Be Visible    id=locator
|        Run Keyword If       '${is_element_visible}'=='True'     Click Element   id=locator

WithLibrary.robot

|    ***** Settings *****
|    Library      SeleniumLibrary
|    Library      DoesIsLibrary
|
|    ***** Test Cases *****
|    WithLibrary
|        ${are_equal}=         Is Equal As Numbers     10     10
|        Run Keyword If        '${are_equal}'=='True'     Log     Equal!
|        Open Browser          http://example.local     gc
|        ${is_element_visible}=        Is Element Visible    id=locator
|        Run Keyword If        '${is_element_visible}'=='True'     Click Element   id=locator


Library Does not provide almost any "static" keywords, except `List Is Keywords` and `List Does keywords` which log names of newly dynamically generated keywords in RF log.html file.

How it works and limitations
----------------------------

Library is looking for imported libraries from ***Settings*** section during start suite phase and then looks for keyword having 'should' in keyword name. Then new keywords are created for each imported library respectively.
As (for now) new keyword generation is triggerd in suite setup phase, new keywords *will not be generated* for libraries imported with RF built in keyword `Import Library`


Example list of generated keywords below:
| BuiltIn             Does Contain                           Should Contain                                    ['container', 'item', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Contain Any                       Should Contain Any                                ['container', '*items', '**configuration']        
| BuiltIn             Does Contain X Times                   Should Contain X Times                            ['container', 'item', 'count', 'msg=None', 'ignore_case=False']
| BuiltIn             Does End With                          Should End With                                   ['str1', 'str2', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Keyword Exist                     Keyword Should Exist                              ['name', 'msg=None']                              
| BuiltIn             Does Match                             Should Match                                      ['string', 'pattern', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Match Regexp                      Should Match Regexp                               ['string', 'pattern', 'msg=None', 'values=True']  
| BuiltIn             Does Not Contain                       Should Not Contain                                ['container', 'item', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Not Contain Any                   Should Not Contain Any                            ['container', '*items', '**configuration']        
| BuiltIn             Does Not End With                      Should Not End With                               ['str1', 'str2', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Not Match                         Should Not Match                                  ['string', 'pattern', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Not Match Regexp                  Should Not Match Regexp                           ['string', 'pattern', 'msg=None', 'values=True']  
| BuiltIn             Does Not Start With                    Should Not Start With                             ['str1', 'str2', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Start With                        Should Start With                                 ['str1', 'str2', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Does Variable Exist                    Variable Should Exist                             ['name', 'msg=None']                              
| BuiltIn             Does Variable Not Exist                Variable Should Not Exist                         ['name', 'msg=None']                              
| BuiltIn             Is Empty                               Should Be Empty                                   ['item', 'msg=None']                              
| BuiltIn             Is Equal                               Should Be Equal                                   ['first', 'second', 'msg=None', 'values=True', 'ignore_case=False', 'formatter=str']
| BuiltIn             Is Equal As Integers                   Should Be Equal As Integers                       ['first', 'second', 'msg=None', 'values=True', 'base=None']
| BuiltIn             Is Equal As Numbers                    Should Be Equal As Numbers                        ['first', 'second', 'msg=None', 'values=True', 'precision=6']
| BuiltIn             Is Equal As Strings                    Should Be Equal As Strings                        ['first', 'second', 'msg=None', 'values=True', 'ignore_case=False', 'formatter=str']
| BuiltIn             Is Length                              Length Should Be                                  ['item', 'length', 'msg=None']                    
| BuiltIn             Is Not Empty                           Should Not Be Empty                               ['item', 'msg=None']                              
| BuiltIn             Is Not Equal                           Should Not Be Equal                               ['first', 'second', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Is Not Equal As Integers               Should Not Be Equal As Integers                   ['first', 'second', 'msg=None', 'values=True', 'base=None']
| BuiltIn             Is Not Equal As Numbers                Should Not Be Equal As Numbers                    ['first', 'second', 'msg=None', 'values=True', 'precision=6']
| BuiltIn             Is Not Equal As Strings                Should Not Be Equal As Strings                    ['first', 'second', 'msg=None', 'values=True', 'ignore_case=False']
| BuiltIn             Is Not True                            Should Not Be True                                ['condition', 'msg=None']                         
| BuiltIn             Is True                                Should Be True                                    ['condition', 'msg=None']                         
| OperatingSystem     Does Directory Exist                   Directory Should Exist                            ['path', 'msg=None']                              
| OperatingSystem     Does Directory Not Exist               Directory Should Not Exist                        ['path', 'msg=None']                              
| OperatingSystem     Does Exist                             Should Exist                                      ['path', 'msg=None']                              
| OperatingSystem     Does File Exist                        File Should Exist                                 ['path', 'msg=None']                              
| OperatingSystem     Does File Not Exist                    File Should Not Exist                             ['path', 'msg=None']                              
| OperatingSystem     Does Not Exist                         Should Not Exist                                  ['path', 'msg=None']                              
| OperatingSystem     Is Directory Empty                     Directory Should Be Empty                         ['path', 'msg=None']                              
| OperatingSystem     Is Directory Not Empty                 Directory Should Not Be Empty                     ['path', 'msg=None']                              
| OperatingSystem     Is Environment Variable Not Set        Environment Variable Should Not Be Set            ['name', 'msg=None']                              
| OperatingSystem     Is Environment Variable Set            Environment Variable Should Be Set                ['name', 'msg=None']                              
| OperatingSystem     Is File Empty                          File Should Be Empty                              ['path', 'msg=None']                              
| OperatingSystem     Is File Not Empty                      File Should Not Be Empty                          ['path', 'msg=None']                              
| Process             Is Process Running                     Process Should Be Running                         ['handle=None', 'error_message=Process is not running.']
| Process             Is Process Stopped                     Process Should Be Stopped                         ['handle=None', 'error_message=Process is running.']
| SSHLibrary          Does Directory Exist                   Directory Should Exist                            ['path']                                          
| SSHLibrary          Does Directory Not Exist               Directory Should Not Exist                        ['path']                                          
| SSHLibrary          Does File Exist                        File Should Exist                                 ['path']                                          
| SSHLibrary          Does File Not Exist                    File Should Not Exist                             ['path']                                          
| SeleniumLibrary     Does Current Frame Contain             Current Frame Should Contain                      ['text', 'loglevel=TRACE']                        
| SeleniumLibrary     Does Current Frame Not Contain         Current Frame Should Not Contain                  ['text', 'loglevel=TRACE']                        
| SeleniumLibrary     Does Element Contain                   Element Should Contain                            ['locator', 'expected', 'message=None', 'ignore_case=False']
| SeleniumLibrary     Does Element Not Contain               Element Should Not Contain                        ['locator', 'expected', 'message=None', 'ignore_case=False']
| SeleniumLibrary     Does Frame Contain                     Frame Should Contain                              ['locator', 'text', 'loglevel=TRACE']             
| SeleniumLibrary     Does List Have No Selections           List Should Have No Selections                    ['locator']                                       
| SeleniumLibrary     Does Location Contain                  Location Should Contain                           ['expected', 'message=None']                      
| SeleniumLibrary     Does Locator Match X Times             Locator Should Match X Times                      ['locator', 'x', 'message=None', 'loglevel=TRACE']
| SeleniumLibrary     Does Page Contain                      Page Should Contain                               ['text', 'loglevel=TRACE']                        
| SeleniumLibrary     Does Page Contain Button               Page Should Contain Button                        ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Contain Checkbox             Page Should Contain Checkbox                      ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Contain Element              Page Should Contain Element                       ['locator', 'message=None', 'loglevel=TRACE', 'limit=None']
| SeleniumLibrary     Does Page Contain Image                Page Should Contain Image                         ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Contain Link                 Page Should Contain Link                          ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Contain List                 Page Should Contain List                          ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Contain Radio Button         Page Should Contain Radio Button                  ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Contain Textfield            Page Should Contain Textfield                     ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain                  Page Should Not Contain                           ['text', 'loglevel=TRACE']                        
| SeleniumLibrary     Does Page Not Contain Button           Page Should Not Contain Button                    ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain Checkbox         Page Should Not Contain Checkbox                  ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain Element          Page Should Not Contain Element                   ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain Image            Page Should Not Contain Image                     ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain Link             Page Should Not Contain Link                      ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain List             Page Should Not Contain List                      ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain Radio Button     Page Should Not Contain Radio Button              ['locator', 'message=None', 'loglevel=TRACE']     
| SeleniumLibrary     Does Page Not Contain Textfield        Page Should Not Contain Textfield                 ['locator', 'message=None', 'loglevel=TRACE']
| SeleniumLibrary     Does Table Cell Contain                Table Cell Should Contain                         ['locator', 'row', 'column', 'expected', 'loglevel=TRACE']
| SeleniumLibrary     Does Table Column Contain              Table Column Should Contain                       ['locator', 'column', 'expected', 'loglevel=TRACE']
| SeleniumLibrary     Does Table Contain                     Table Should Contain                              ['locator', 'expected', 'loglevel=TRACE']         
| SeleniumLibrary     Does Table Footer Contain              Table Footer Should Contain                       ['locator', 'expected', 'loglevel=TRACE']         
| SeleniumLibrary     Does Table Header Contain              Table Header Should Contain                       ['locator', 'expected', 'loglevel=TRACE']         
| SeleniumLibrary     Does Table Row Contain                 Table Row Should Contain                          ['locator', 'row', 'expected', 'loglevel=TRACE']  
| SeleniumLibrary     Does Textarea Contain                  Textarea Should Contain                           ['locator', 'expected', 'message=None']           
| SeleniumLibrary     Does Textfield Contain                 Textfield Should Contain                          ['locator', 'expected', 'message=None']           
| SeleniumLibrary     Is Alert Not Present                   Alert Should Not Be Present                       ['action=ACCEPT', 'timeout=0']                    
| SeleniumLibrary     Is Alert Present                       Alert Should Be Present                           ['text=', 'action=ACCEPT', 'timeout=None']        
| SeleniumLibrary     Is Checkbox Not Selected               Checkbox Should Not Be Selected                   ['locator']                                       
| SeleniumLibrary     Is Checkbox Selected                   Checkbox Should Be Selected                       ['locator']                                       
| SeleniumLibrary     Is Element Attribute Value             Element Attribute Value Should Be                 ['locator', 'attribute', 'expected', 'message=None']
| SeleniumLibrary     Is Element Disabled                    Element Should Be Disabled                        ['locator']                                       
| SeleniumLibrary     Is Element Enabled                     Element Should Be Enabled                         ['locator']                                       
| SeleniumLibrary     Is Element Focused                     Element Should Be Focused                         ['locator']                                       
| SeleniumLibrary     Is Element Not Visible                 Element Should Not Be Visible                     ['locator', 'message=None']                       
| SeleniumLibrary     Is Element Text                        Element Text Should Be                            ['locator', 'expected', 'message=None', 'ignore_case=False']
| SeleniumLibrary     Is Element Text Not                    Element Text Should Not Be                        ['locator', 'not_expected', 'message=None', 'ignore_case=False']
| SeleniumLibrary     Is Element Visible                     Element Should Be Visible                         ['locator', 'message=None']                       
| SeleniumLibrary     Is List Selection                      List Selection Should Be                          ['locator', '*expected']                          
| SeleniumLibrary     Is Location                            Location Should Be                                ['url', 'message=None']                           
| SeleniumLibrary     Is Radio Button Not Selected           Radio Button Should Not Be Selected               ['group_name']
| SeleniumLibrary     Is Radio Button Set To                 Radio Button Should Be Set To                     ['group_name', 'value']                           
| SeleniumLibrary     Is Textarea Value                      Textarea Value Should Be                          ['locator', 'expected', 'message=None']           
| SeleniumLibrary     Is Textfield Value                     Textfield Value Should Be                         ['locator', 'expected', 'message=None']           
| SeleniumLibrary     Is Title                               Title Should Be                                   ['title', 'message=None']                         
| String              Is Byte String                         Should Be Byte String                             ['item', 'msg=None']                              
| String              Is Lowercase                           Should Be Lowercase                               ['string', 'msg=None']                            
| String              Is Not String                          Should Not Be String                              ['item', 'msg=None']                              
| String              Is String                              Should Be String                                  ['item', 'msg=None']                              
| String              Is Titlecase                           Should Be Titlecase                               ['string', 'msg=None']                            
| String              Is Unicode String                      Should Be Unicode String                          ['item', 'msg=None']                              
| String              Is Uppercase                           Should Be Uppercase                               ['string', 'msg=None']                            




    """


