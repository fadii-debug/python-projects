class Person:
    def introduce(self):
        print("I am a person.")


class Teacher(Person):
    def teach(self):
        print("I teach students.")


class Developer:
    def code(self):
        print("I write code.")


class SeniorTrainer(Teacher, Developer):
    def guide(self):
        print("I guide junior trainer.")


st=SeniorTrainer()

st.introduce()
st.teach()
st.code()
st.guide()
print(SeniorTrainer.mro())