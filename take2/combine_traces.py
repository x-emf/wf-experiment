import json, os

import cfg

def traceno(s):
	if "(" not in s and ")" not in s:
		return 0
	else:
		op, cp = s.index("("), s.index(")")
		return int(s[op+1:cp])

alltraces, filecount = [], 0

print("Merging traces in original_traces/...")
for i in sorted(os.listdir("original_traces"), key=traceno):
	print(f"Reading {i}...")
	filecount += 1
	with open(f"original_traces/{i}", "r") as f:
		otrace_obj = json.load(f)
		traces = otrace_obj["traces"]
		alltraces.extend(traces)
		print(f"Added {len(traces)} traces. ")
print(f"Merged {len(alltraces)} traces from {filecount} files.")
print("Done merging traces.")

print("Attaching class information...")
traces_with_class = []
class_index = 0
for trace in alltraces:
	traces_with_class.append({
		"trace": trace,
		"class": class_index,
	})
	class_index = (class_index + 1) % cfg.N_CLASSES

final_obj = {
	"data": traces_with_class,
}

print("Attached class information to all traces.")

ser_target = "alldata.json"
print(f"Serialization target is \"{ser_target}\" in cwd.")
print(f"Serializing {{\"data\": <{len(traces_with_class)} item list>}}...")

with open(ser_target, "w") as f:
	json.dump(final_obj, f)
print("Serialization complete. All done.")
