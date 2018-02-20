class Person:
  def wake_up(self):
    return "Hello, World!"

@Given('^a person$')
def a_person(self):
  self.person = Person()

@When('^that person wakes up$')
def that_person_wakes_up(self):
  self.last_response = self.person.wake_up()

@Then('^that person says "([^"]*)"$')
def that_person_says(self, arg1):
  if (arg1 != self.last_response):
    raise(Exception("person said '%s' not '%s'" % (self.last_response, arg1)))
