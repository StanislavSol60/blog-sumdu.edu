import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://127.0.0.1:5000/')

WebUI.maximizeWindow()

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/a_Sign Up'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Blog/input_Sign Up_email'), 'test.comments@gmail.com')

WebUI.setText(findTestObject('Object Repository/Page_Flask Blog/input_Sign Up_name'), 'test comments')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Blog/input_Sign Up_password'), 'RigbBhfdqOBGNlJIWM1ClA==')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Blog/input_Sign Up_confirm_password'), 'RigbBhfdqOBGNlJIWM1ClA==')

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/button_Sign Up'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Blog/input_Congratulations, you are now a regist_b591c9'), 'test.comments@gmail.com')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Blog/input_Congratulations, you are now a regist_d71d15'), 
    'RigbBhfdqOBGNlJIWM1ClA==')

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/button_Login'))

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/a_Create New Post'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Blog/input_Title_title'), 'test comment title')

WebUI.setText(findTestObject('Object Repository/Page_Flask Blog/textarea_Content_content'), 'test comment content')

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/button_Submit'))

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/a_Home'))

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/a_test comment title'))

WebUI.setText(findTestObject('Page_Flask Blog/textarea_Content_comment'), 'test comment comment')

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/button_Add Comment'))

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/a_Logout'))

WebUI.click(findTestObject('Object Repository/Page_Flask Blog/div_Login                                  _89807f'))

WebUI.closeBrowser()

