from utils.driver_factory import DriverFactory
import allure


def before_scenario(context, scenario):
    context.driver = DriverFactory.get_driver()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="Failure Screenshot",
                      attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    context.driver.quit()
