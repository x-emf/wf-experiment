import pyautogui as agui

import time

def clickCollectTraces():
	agui.moveTo(125, 273)
	agui.leftClick()
	time.sleep(1)

def openSecondTab():
	agui.moveTo(268, 45)
	agui.leftClick()
	time.sleep(1)

def closeSecondTab():
	agui.moveTo(472, 50)
	agui.leftClick()
	time.sleep(1)

def collectSample(website):
	closeSecondTab()
	clickCollectTraces()
	openSecondTab()
	agui.write(website, interval=(2/len(website)))
	time.sleep(0.5)
	agui.write(['enter'])
	time.sleep(7 + 1)
	closeSecondTab()

def downloadTraces():
	agui.moveTo(290, 278)
	agui.leftClick()
	time.sleep(5)

def refreshPage():
	agui.moveTo(90, 83)
	agui.leftClick()
	time.sleep(5)

websites = [
	"adafruit.com",
	"reddit.com",
	"discord.com",
	"opensecrets.org",
	"amazon.com",
]

trials_per_class = 100

print("Starting data collection...")
print("--- --- ---")

index = 0
durations = []
for i in range(trials_per_class):
	for j, site in enumerate(websites):
		print(f"#debug: starting trace with sitenum={j}...")
		print(f"#debug: sitenum={j} means \"{site}\"")
		start = time.time()
		collectSample(site)
		duration = time.time() - start
		durations.append(duration)
		durations = durations[-10:]
		mean_duration = sum(durations) / len(durations)
		samples_left = (trials_per_class * len(websites)) - index - 1
		eta_s = int(mean_duration) * samples_left
		eta_m, eta_s = divmod(eta_s, 60)
		eta_h, eta_m = divmod(eta_m, 60)
		print(f"#debug: done collecting trace.")
		print(f"#debug: DURATION = {duration:.2f}s")
		print(f"#debug: ETA = {eta_h}h{eta_m}m{eta_s}s")
		print(f"#debug: trialnum={i}, sitenum={j}, index={index}")
		print(f">>GOT>> {index} -> {j}")
		print(f"--- --- ---")
		if index >= len(websites) * 5:
			print(f"#debug: index too high, download+refresh")
			print(f"#debug: downloading traces...")
			downloadTraces()
			print(f"#debug: /!\\ refreshing the page... /!\\")
			refreshPage()
			index = 0
			print(f"#debug: download+refresh done, index reset")
		else:
			index += 1
