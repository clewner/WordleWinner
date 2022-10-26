from pynput.keyboard import *
from pynput.keyboard import Key, Controller
from PIL import Image
from PIL import ImageGrab
import time
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

keyboard = Controller()


def press_on(key):
	if key == Key.end:
		quit()
		
	if key == Key.space:
		keyboard.press("g")
		keyboard.release("g")

		keyboard.press("l")
		keyboard.release("l")

		keyboard.press("e")
		keyboard.release("e")

		keyboard.press("n")
		keyboard.release("n")

		keyboard.press("t")
		keyboard.release("t")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.3)
		keyboard.press("b")
		keyboard.release("b")

		keyboard.press("r")
		keyboard.release("r")

		keyboard.press("i")
		keyboard.release("i")

		keyboard.press("c")
		keyboard.release("c")

		keyboard.press("k")
		keyboard.release("k")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.5)
		keyboard.press("j")
		keyboard.release("j")

		keyboard.press("u")
		keyboard.release("u")

		keyboard.press("m")
		keyboard.release("m")

		keyboard.press("p")
		keyboard.release("p")

		keyboard.press("y")
		keyboard.release("y")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.7)

		keyboard.press("v")
		keyboard.release("v")

		keyboard.press("o")
		keyboard.release("o")

		keyboard.press("z")
		keyboard.release("z")

		keyboard.press("h")
		keyboard.release("h")

		keyboard.press("d")
		keyboard.release("d")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.5)

		keyboard.press("w")
		keyboard.release("w")

		keyboard.press("a")
		keyboard.release("a")

		keyboard.press("q")
		keyboard.release("q")

		keyboard.press("f")
		keyboard.release("f")

		keyboard.press("s")
		keyboard.release("s")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		
		time.sleep(0.5)
		im2 = ImageGrab.grab(bbox = None, all_screens = False)
		results = []
		pixels = im2.load()
		
		for j in range(5):
			for i in range(5):
				if pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (83, 141, 78):
					results.append("green")
					pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] = (255,0,0)
				elif pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (181, 159, 59):
					results.append("yellow")
					pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] = (255,0,0)
				else:
					results.append("grey")
					pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] = (255,0,0)
		
		
		print(results)
		answer = []

		url = "https://notfunatparties.com/wordle-solver"

		s = Service('C:/Users/isaac/Downloads/chromedriver_win32/chromedriver.exe')
		driver = webdriver.Chrome(service=s)

		driver.get(url)

		#first word
		inputList = driver.find_elements(By.CLASS_NAME, "h-16")
		inputList[0].send_keys("g")
		inputList[1].send_keys("l")
		inputList[2].send_keys("e")
		inputList[3].send_keys("n")
		inputList[4].send_keys("t")

		greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
		blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
		yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")

		for i in range(5):
			if results[i] == "yellow":
				yellowButton[i].click()
			elif results[i] == "green":
				greenButton[i].click()
			else:
				blackButton[i].click()

		final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
		final.click()

		#second word

		last = driver.find_elements(By.CLASS_NAME, "py-2")

		if(last[0].text == "Solved!"):
			print("DONE: ")

			newInputList = driver.find_elements(By.CLASS_NAME, "h-16")

			print(newInputList[len(newInputList) - 5].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
			print(newInputList[len(newInputList) - 4].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
			print(newInputList[len(newInputList) - 3].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
			print(newInputList[len(newInputList) - 2].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
			print(newInputList[len(newInputList) - 1].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
			driver.quit()

		elif(last[0].text == "I think you screwed up"):
			answer = []
			print(last[0].text)
			driver.quit()

		else:
			inputList = driver.find_elements(By.CLASS_NAME, "h-16")
			inputList[5].send_keys("b")
			inputList[6].send_keys("r")
			inputList[7].send_keys("i")
			inputList[8].send_keys("c")
			inputList[9].send_keys("k")

			greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
			blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
			yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
			for i in range(5):
				if results[i + 5] == "yellow":
					yellowButton[i].click()
				elif results[i + 5] == "green":
					greenButton[i].click()
				else:
					blackButton[i].click()

			final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
			final.click()

			#3rd word
			last = driver.find_elements(By.CLASS_NAME, "py-2")
			if(last[0].text == "Solved!"):
				print("DONE: ")
				newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
				print(newInputList[len(newInputList) - 5].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
				print(newInputList[len(newInputList) - 4].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
				print(newInputList[len(newInputList) - 3].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
				print(newInputList[len(newInputList) - 2].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
				print(newInputList[len(newInputList) - 1].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
				driver.quit()

			elif(last[0].text == "I think you screwed up"):
				answer = []
				print(last[0].text)
				driver.quit()
			else:

				inputList = driver.find_elements(By.CLASS_NAME, "h-16")
				inputList[10].send_keys("j")
				inputList[11].send_keys("u")
				inputList[12].send_keys("m")
				inputList[13].send_keys("p")
				inputList[14].send_keys("y")

				greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
				blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
				yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
				for i in range(5):
					if results[i + 10] == "yellow":
						yellowButton[i].click()
					elif results[i + 10] == "green":
						greenButton[i].click()
					else:
						blackButton[i].click()

				final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
				final.click()

				#4th word
				last = driver.find_elements(By.CLASS_NAME, "py-2")
				if(last[0].text == "Solved!"):
					print("DONE: ")
					newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
					print(newInputList[len(newInputList) - 5].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
					print(newInputList[len(newInputList) - 4].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
					print(newInputList[len(newInputList) - 3].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
					print(newInputList[len(newInputList) - 2].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
					print(newInputList[len(newInputList) - 1].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
					driver.quit()

				elif(last[0].text == "I think you screwed up"):
					answer = []
					print(last[0].text)
					driver.quit()

				else:
					inputList = driver.find_elements(By.CLASS_NAME, "h-16")
					inputList[15].send_keys("v")
					inputList[16].send_keys("o")
					inputList[17].send_keys("z")
					inputList[18].send_keys("h")
					inputList[19].send_keys("d")

					greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
					blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
					yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
					for i in range(5):
						if results[i + 15] == "yellow":
							yellowButton[i].click()
						elif results[i + 15] == "green":
							greenButton[i].click()
						else:
							blackButton[i].click()

					final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
					final.click()

					last = driver.find_elements(By.CLASS_NAME, "py-2")
					if(last[0].text == "Solved!"):
						print("DONE: ")
						newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
						print(newInputList[len(newInputList) - 5].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
						print(newInputList[len(newInputList) - 4].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
						print(newInputList[len(newInputList) - 3].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
						print(newInputList[len(newInputList) - 2].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
						print(newInputList[len(newInputList) - 1].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
						driver.quit()

					elif(last[0].text == "I think you screwed up"):
						answer = []
						print(last[0].text)
						driver.quit()
					else:
						inputList = driver.find_elements(By.CLASS_NAME, "h-16")
						inputList[20].send_keys("W")
						inputList[21].send_keys("A")
						inputList[22].send_keys("Q")
						inputList[23].send_keys("F")
						inputList[24].send_keys("S")

						greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
						blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
						yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
						for i in range(5):
							if results[i + 20] == "yellow":
								yellowButton[i].click()
							elif results[i + 20] == "green":
								greenButton[i].click()
							else:
								blackButton[i].click()

						final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
						final.click()

						last = driver.find_elements(By.CLASS_NAME, "py-2")
						print(last[0].text)
						if(last[0].text == "I think you screwed up"):
							answer = []
							print(last[0].text)
							driver.quit()
							
						else:
							newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
							print(newInputList[len(newInputList) - 5].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
							print(newInputList[len(newInputList) - 4].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
							print(newInputList[len(newInputList) - 3].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
							print(newInputList[len(newInputList) - 2].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
							print(newInputList[len(newInputList) - 1].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
							driver.minimize_window()
			
		
		for i in answer:
			keyboard.press(str(i))
			keyboard.release(str(i))

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

	elif key == Key.home:
		keyboard.press("t")
		keyboard.release("t")

		keyboard.press("a")
		keyboard.release("a")

		keyboard.press("l")
		keyboard.release("l")

		keyboard.press("o")
		keyboard.release("o")

		keyboard.press("n")
		keyboard.release("n")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.3)
		keyboard.press("s")
		keyboard.release("s")

		keyboard.press("u")
		keyboard.release("u")

		keyboard.press("r")
		keyboard.release("r")

		keyboard.press("g")
		keyboard.release("g")

		keyboard.press("e")
		keyboard.release("e")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.5)
		keyboard.press("w")
		keyboard.release("w")

		keyboard.press("i")
		keyboard.release("i")

		keyboard.press("c")
		keyboard.release("c")

		keyboard.press("k")
		keyboard.release("k")

		keyboard.press("y")
		keyboard.release("y")

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		
		time.sleep(0.5)
		im2 = ImageGrab.grab(bbox = None, all_screens = False)
		results = []
		pixels = im2.load()
		
		for j in range(3):
			for i in range(5):
				if pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (83, 141, 78):
					results.append("green")
					
				elif pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (181, 159, 59):
					results.append("yellow")
					
				else:
					results.append("grey")
					

		print(results)
		answer = []
		nextTry = []

		url = "https://notfunatparties.com/wordle-solver"

		s = Service('C:/Users/isaac/Downloads/chromedriver_win32/chromedriver.exe')
		driver = webdriver.Chrome(service=s)

		driver.get(url)

		#first word
		inputList = driver.find_elements(By.CLASS_NAME, "h-16")
		inputList[0].send_keys("t")
		inputList[1].send_keys("a")
		inputList[2].send_keys("l")
		inputList[3].send_keys("o")
		inputList[4].send_keys("n")

		greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
		blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
		yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")

		for i in range(5):
			if results[i] == "yellow":
				yellowButton[i].click()
			elif results[i] == "green":
				greenButton[i].click()
			else:
				blackButton[i].click()

		final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
		final.click()

		#second word

		last = driver.find_elements(By.CLASS_NAME, "py-2")

		if(last[0].text == "Solved!"):
			print("DONE: ")

			newInputList = driver.find_elements(By.CLASS_NAME, "h-16")

			print(newInputList[len(newInputList) - 5].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
			print(newInputList[len(newInputList) - 4].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
			print(newInputList[len(newInputList) - 3].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
			print(newInputList[len(newInputList) - 2].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
			print(newInputList[len(newInputList) - 1].get_attribute('value'))
			answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
			driver.minimize_window()

		elif(last[0].text == "I think you screwed up"):
				answer = []
				print(last[0].text)
				driver.quit()

		else:
			inputList = driver.find_elements(By.CLASS_NAME, "h-16")
			inputList[5].send_keys("s")
			inputList[6].send_keys("u")
			inputList[7].send_keys("r")
			inputList[8].send_keys("g")
			inputList[9].send_keys("e")

			greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
			blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
			yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
			for i in range(5):
				if results[i + 5] == "yellow":
					yellowButton[i].click()
				elif results[i + 5] == "green":
					greenButton[i].click()
				else:
					blackButton[i].click()

			final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
			final.click()

			#3rd word
			last = driver.find_elements(By.CLASS_NAME, "py-2")
			if(last[0].text == "Solved!"):
				print("DONE: ")
				newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
				print(newInputList[len(newInputList) - 5].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
				print(newInputList[len(newInputList) - 4].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
				print(newInputList[len(newInputList) - 3].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
				print(newInputList[len(newInputList) - 2].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
				print(newInputList[len(newInputList) - 1].get_attribute('value'))
				answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
				driver.minimize_window()

			elif(last[0].text == "I think you screwed up"):
				answer = []
				print(last[0].text)
				driver.quit()

			else:

				inputList = driver.find_elements(By.CLASS_NAME, "h-16")
				inputList[10].send_keys("w")
				inputList[11].send_keys("i")
				inputList[12].send_keys("c")
				inputList[13].send_keys("k")
				inputList[14].send_keys("y")

				greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
				blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
				yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
				for i in range(5):
					if results[i + 10] == "yellow":
						yellowButton[i].click()
					elif results[i + 10] == "green":
						greenButton[i].click()
					else:
						blackButton[i].click()

				final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
				final.click()

				last = driver.find_elements(By.CLASS_NAME, "py-2")
				if(last[0].text == "Solved!"):
					print("DONE: ")
					newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
					print(newInputList[len(newInputList) - 5].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
					print(newInputList[len(newInputList) - 4].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
					print(newInputList[len(newInputList) - 3].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
					print(newInputList[len(newInputList) - 2].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
					print(newInputList[len(newInputList) - 1].get_attribute('value'))
					answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
					driver.minimize_window()
				elif(last[0].text == "I think you screwed up"):
					print(last[0].text)
					driver.quit()
					answer = []
				else:
					newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
					print(newInputList[len(newInputList) - 5].get_attribute('value'))
					nextTry.append(newInputList[len(newInputList) - 5].get_attribute('value'))
					print(newInputList[len(newInputList) - 4].get_attribute('value'))
					nextTry.append(newInputList[len(newInputList) - 4].get_attribute('value'))
					print(newInputList[len(newInputList) - 3].get_attribute('value'))
					nextTry.append(newInputList[len(newInputList) - 3].get_attribute('value'))
					print(newInputList[len(newInputList) - 2].get_attribute('value'))
					nextTry.append(newInputList[len(newInputList) - 2].get_attribute('value'))
					print(newInputList[len(newInputList) - 1].get_attribute('value'))
					nextTry.append(newInputList[len(newInputList) - 1].get_attribute('value'))
					driver.minimize_window()
					for i in nextTry:
						keyboard.press(str(i))
						keyboard.release(str(i))


					keyboard.press(Key.enter)
					keyboard.release(Key.enter)
					time.sleep(0.5)
					im2 = ImageGrab.grab(bbox = None, all_screens = False)
					results = []
					pixels = im2.load()
					for j in range(4):
						for i in range(5):
							if pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (83, 141, 78):
								results.append("green")
								
							elif pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (181, 159, 59):
								results.append("yellow")
								
							else:
								results.append("grey")


					driver.maximize_window()
					inputList = driver.find_elements(By.CLASS_NAME, "h-16")
					inputList[15].send_keys(str(nextTry[0]))
					inputList[16].send_keys(str(nextTry[1]))
					inputList[17].send_keys(str(nextTry[2]))
					inputList[18].send_keys(str(nextTry[3]))
					inputList[19].send_keys(str(nextTry[4]))

					greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
					blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
					yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
					for i in range(5):
						if results[i + 15] == "yellow":
							yellowButton[i].click()
						elif results[i + 15] == "green":
							greenButton[i].click()
						else:
							blackButton[i].click()

					final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
					final.click()

					last = driver.find_elements(By.CLASS_NAME, "py-2")
					if(last[0].text == "Solved!"):
						print("DONE: ")
						newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
						print(newInputList[len(newInputList) - 5].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
						print(newInputList[len(newInputList) - 4].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
						print(newInputList[len(newInputList) - 3].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
						print(newInputList[len(newInputList) - 2].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
						print(newInputList[len(newInputList) - 1].get_attribute('value'))
						answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
						driver.minimize_window()
					elif(last[0].text == "I think you screwed up"):
						print(last[0].text)
						driver.quit()
						answer = []
					else:
						nextTry = []
						newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
						print(newInputList[len(newInputList) - 5].get_attribute('value'))
						nextTry.append(newInputList[len(newInputList) - 5].get_attribute('value'))
						print(newInputList[len(newInputList) - 4].get_attribute('value'))
						nextTry.append(newInputList[len(newInputList) - 4].get_attribute('value'))
						print(newInputList[len(newInputList) - 3].get_attribute('value'))
						nextTry.append(newInputList[len(newInputList) - 3].get_attribute('value'))
						print(newInputList[len(newInputList) - 2].get_attribute('value'))
						nextTry.append(newInputList[len(newInputList) - 2].get_attribute('value'))
						print(newInputList[len(newInputList) - 1].get_attribute('value'))
						nextTry.append(newInputList[len(newInputList) - 1].get_attribute('value'))
						driver.minimize_window()
						for i in nextTry:
							keyboard.press(str(i))
							keyboard.release(str(i))

						keyboard.press(Key.enter)
						keyboard.release(Key.enter)
						time.sleep(0.5)
						im2 = ImageGrab.grab(bbox = None, all_screens = False)
						results = []
						pixels = im2.load()
						for j in range(5):
							for i in range(5):
								if pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (83, 141, 78):
									results.append("green")
									
								elif pixels[int((im2.size[0])*0.09) + int((im2.size[0])*0.07) * i, int((im2.size[1])*0.22) + int((im2.size[1])*0.085) * j] == (181, 159, 59):
									results.append("yellow")
									
								else:
									results.append("grey")

						driver.maximize_window()
						inputList = driver.find_elements(By.CLASS_NAME, "h-16")
						inputList[20].send_keys(str(nextTry[0]))
						inputList[21].send_keys(str(nextTry[1]))
						inputList[22].send_keys(str(nextTry[2]))
						inputList[23].send_keys(str(nextTry[3]))
						inputList[24].send_keys(str(nextTry[4]))

						greenButton = driver.find_elements(By.CLASS_NAME, "bg-green-500")
						blackButton = driver.find_elements(By.CLASS_NAME, "bg-gray-800")
						yellowButton = driver.find_elements(By.CSS_SELECTOR, "button[class*='md:w-4 bg-yellow-500']")
						for i in range(5):
							if results[i + 20] == "yellow":
								yellowButton[i].click()
							elif results[i + 20] == "green":
								greenButton[i].click()
							else:
								blackButton[i].click()

						final = driver.find_element(By.CLASS_NAME, "bg-indigo-600")
						final.click()

						last = driver.find_elements(By.CLASS_NAME, "py-2")
						if(last[0].text == "I think you screwed up"):
							print(last[0].text)
							answer = []
							driver.quit()
							
						else:
							newInputList = driver.find_elements(By.CLASS_NAME, "h-16")
							print(newInputList[len(newInputList) - 5].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 5].get_attribute('value'))
							print(newInputList[len(newInputList) - 4].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 4].get_attribute('value'))
							print(newInputList[len(newInputList) - 3].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 3].get_attribute('value'))
							print(newInputList[len(newInputList) - 2].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 2].get_attribute('value'))
							print(newInputList[len(newInputList) - 1].get_attribute('value'))
							answer.append(newInputList[len(newInputList) - 1].get_attribute('value'))
							driver.minimize_window()

		for i in answer:
			keyboard.press(str(i))
			keyboard.release(str(i))

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		driver.quit()




with Listener(on_press = press_on) as listener:
	listener.join()




"""
GLENT
BRICK
JUMPY
VOZHD
WAQFS
"""
