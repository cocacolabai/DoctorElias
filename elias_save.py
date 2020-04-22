# tasks
# Consider all symptoms.
# Build engine
# Take severity symptoms: 0-5 scale, 0 being not at all, 5 meaning extremely severe.

# Libraries
from experta import *

symptoms_list = ['headache', 'back pain', 'chest pain', 'cough', 'fainting', 'fatigue', 'sunken eyes', 'low body temperature', 
				'restlesness', 'sore throat', 'fever', 'nausea', 'blurred vision']

# Diseases:   [0,0,0,0,0,0,0,0,0,0,0,0,0]
diseases_dict = ["Alzheimers", "Arthritis", "Asthma", "Diabetes", "Epilepsy", "Glaucoma", "Heart Disease", "Heat Stroke",
				"Hyperthyroidism", "Hypothermia", "Jaundice", "Sinusitis", "Tuberculosis"]

symptoms_disease_map = [
[0,0,0,0,0,0,0,1,0,0,0,0,0]
,[0,1,0,0,0,0,1,0,0,0,0,0,0]
,[0,0,1,1,0,0,0,1,0,0,0,0,0]
,[0,0,0,0,0,0,1,0,0,0,0,1,1]
,[0,0,0,0,0,0,1,0,0,0,0,0,0]
,[1,0,0,0,0,0,0,0,0,0,0,1,1]
,[0,0,1,0,0,0,0,0,0,0,0,1,0]
,[1,0,0,0,0,0,0,0,0,1,0,1,0]
,[0,0,0,0,0,0,1,0,0,0,0,1,0]
,[0,0,0,0,1,0,0,0,1,0,0,0,0]
,[0,0,0,0,0,0,1,0,0,1,0,1,0]
,[1,0,0,1,0,1,0,0,0,1,0,0,0]
,[0,0,1,1,0,0,0,0,0,1,0,0,0]]

def get_symptoms(disease):
	return symptoms_disease_map[diseases_dict.index(disease)]

# Doctor Class
class DoctorElias(KnowledgeEngine):
	@DefFacts()
	def start(self):
		print("Hey! Welcome to the Olive Wellness Centre, I am Elias! I believe you are here for a checkup. In order to do that, I will need you to ask some questions for me.\n For all these questions, answer with a number between 0 to 5. With 0 meaning that symptom is not present and 5 meaning a severe case of that symptom.\n")
		yield Fact(action = "diagnose")

	@Rule(Fact(action = "diagnose"), NOT(Fact(headache = W())), salience = 1)
	def symptom1(self):
		self.declare(Fact(headache = input("Do you have a headache? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(back_pain = W())), salience = 1)
	def symptom2(self):
		self.declare(Fact(back_pain = input("Do you have back pain? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(chest_pain = W())), salience = 1)
	def symptom3(self):
		self.declare(Fact(chest_pain = input("Do you have chest pain? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(cough = W())), salience = 1)
	def symptom4(self):
		self.declare(Fact(cough = input("Do you have a cough? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(fainting = W())), salience = 1)
	def symptom5(self):
		self.declare(Fact(fainting = input("Do you experience fainting? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(fatigue = W())), salience = 1)
	def symptom6(self):
		self.declare(Fact(fatigue = input("Do you experience fatigue? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(sunken_eyes = W())), salience = 1)
	def symptom7(self):
		self.declare(Fact(sunken_eyes = input("Do you have sunken eyes? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(low_body_temp = W())), salience = 1)
	def symptom8(self):
		self.declare(Fact(low_body_temp = input("Do you have a low body temperature? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(restlessness = W())), salience = 1)
	def symptom9(self):
		self.declare(Fact(restlessness = input("Do you feel restless? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(sore_throat = W())), salience = 1)
	def symptom10(self):
		self.declare(Fact(sore_throat = input("Do you have a sore throat? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(fever = W())), salience = 1)
	def symptom11(self):
		self.declare(Fact(fever = input("Do you have a fever? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(nausea = W())), salience = 1)
	def symptom12(self):
		self.declare(Fact(nausea = input("Do you feel nauseous? ")))

	@Rule(Fact(action = "diagnose"), NOT(Fact(blurred_vision = W())), salience = 1)
	def symptom13(self):
		self.declare(Fact(blurred_vision = input("Do you experience blurred vision? ")))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),NOT(Fact(fatigue="0")),Fact(restlessness="0"),Fact(low_body_temp="0"),NOT(Fact(fever="0")),Fact(sunken_eyes="0"),NOT(Fact(nausea="0")),Fact(blurred_vision="0"))
	def disease_0(self):
		self.declare(Fact(disease="Jaundice"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),Fact(fatigue="0"),NOT(Fact(restlessness="0")),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_1(self):
		self.declare(Fact(disease="Alzheimers"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),NOT(Fact(back_pain="0")),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),NOT(Fact(fatigue="0")),Fact(restlessness="0"),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_2(self):
		self.declare(Fact(disease="Arthritis"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),NOT(Fact(chest_pain="0")),NOT(Fact(cough="0")),Fact(fainting="0"),Fact(sore_throat="0"),Fact(fatigue="0"),Fact(restlessness="0"),Fact(low_body_temp="0"),NOT(Fact(fever="1")),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_3(self):
		self.declare(Fact(disease="Tuberculosis"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),NOT(Fact(chest_pain="0")),NOT(Fact(cough="0")),Fact(fainting="0"),Fact(sore_throat="0"),Fact(fatigue="0"),NOT(Fact(restlessness="0")),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_4(self):
		self.declare(Fact(disease="Asthma"))

	@Rule(Fact(action='diagnose'),NOT(Fact(headache="0")),Fact(back_pain="0"),Fact(chest_pain="0"),NOT(Fact(cough="0")),Fact(fainting="0"),NOT(Fact(sore_throat="0")),Fact(fatigue="0"),Fact(restlessness="0"),Fact(low_body_temp="0"),NOT(Fact(fever="0")),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_5(self):
		self.declare(Fact(disease="Sinusitis"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),NOT(Fact(fatigue="0")),Fact(restlessness="0"),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_6(self):
		self.declare(Fact(disease="Epilepsy"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),NOT(Fact(chest_pain="0")),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),Fact(fatigue="0"),Fact(restlessness="0"),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),NOT(Fact(nausea="0")),Fact(blurred_vision="0"))
	def disease_7(self):
		self.declare(Fact(disease="Heart Disease"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),NOT(Fact(fatigue="0")),Fact(restlessness="0"),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),NOT(Fact(nausea="0")),NOT(Fact(blurred_vision="0")))
	def disease_8(self):
		self.declare(Fact(disease="Diabetes"))

	@Rule(Fact(action='diagnose'),NOT(Fact(headache="0")),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),Fact(fatigue="0"),Fact(restlessness="0"),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),NOT(Fact(nausea="0")),NOT(Fact(blurred_vision="0")))
	def disease_9(self):
		self.declare(Fact(disease="Glaucoma"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),NOT(Fact(fatigue="0")),Fact(restlessness="0"),Fact(low_body_temp="0"),Fact(fever="0"),Fact(sunken_eyes="0"),NOT(Fact(nausea="0")),Fact(blurred_vision="0"))
	def disease_10(self):
		self.declare(Fact(disease="Hyperthyroidism"))

	@Rule(Fact(action='diagnose'),Fact(headache="1"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),Fact(fainting="0"),Fact(sore_throat="0"),Fact(fatigue="0"),Fact(restlessness="0"),Fact(low_body_temp="0"),NOT(Fact(fever="0")),Fact(sunken_eyes="0"),NOT(Fact(nausea="0")),Fact(blurred_vision="0"))
	def disease_11(self):
		self.declare(Fact(disease="Heat Stroke"))

	@Rule(Fact(action='diagnose'),Fact(headache="0"),Fact(back_pain="0"),Fact(chest_pain="0"),Fact(cough="0"),NOT(Fact(fainting="0")),Fact(sore_throat="0"),Fact(fatigue="0"),Fact(restlessness="0"),NOT(Fact(low_body_temp="0")),Fact(fever="0"),Fact(sunken_eyes="0"),Fact(nausea="0"),Fact(blurred_vision="0"))
	def disease_12(self):
		self.declare(Fact(disease="Hypothermia"))

	@Rule(Fact(action='diagnose'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		id_disease = disease
		disease_details = get_symptoms(id_disease)
		print("\nThe disease could mostly be " + str(id_disease))
		print("The rule taken into account was: ")
		for i in range(len(disease_details)):
			if disease_details[i] != 0:
				print("<" + symptoms_list[i] + "> yes.")
			else:
				print("<" + symptoms_list[i] + "> no.")

		print(" --> " + str(id_disease))


	@Rule(Fact(action='diagnose'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def unmatched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		print("\nCould not exactly diagnose what the disease is, but let me try maximum symptom match!")
		dis_lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		max_val = 0
		max_dis = ""
		for i in range(len(symptoms_disease_map)):
			temp_val = 0
			for j in range(len(symptoms_disease_map[i])):
				if dis_lis[j] == str(symptoms_disease_map[i][j]):
					temp_val += 1
				if temp_val > max_val:
					max_val = temp_val
					max_dis = diseases_dict[i]

		id_disease = max_dis
		disease_details = get_symptoms(id_disease)
		print("\nThe disease could mostly be " + str(id_disease))
		print("The rule taken into account was: ")
		for i in range(len(disease_details)):
			if disease_details[i] != 0:
				print("<" + symptoms_list[i] + "> yes.")
			else:
				print("<" + symptoms_list[i] + "> no.")

		print(" --> " + str(id_disease))

if __name__ == "__main__":
	elias = DoctorElias()
	while 1:
		elias.reset()
		elias.run()
		print("Would you like to diagnose some other symptoms?")
		if input() == "no":
			exit()

