from typing import List
from queue import PriorityQueue

class TimeTracker:
	_activities = {}
	_top3 = []
 
	def _update(self, activity: str, time: int) -> None:
		if (activity in self._top3):
			return
		if (len(self._top3) < 3):
			self._top3.append(activity)
			return

		idx = -1
		min_time = time
		for i in range(len(self._top3)):
			curr_time = self._activities[self._top3[i]][1]
			if (curr_time < min_time):
				idx = i
				min_time = curr_time

		if (idx != -1):
			self._top3[idx] = activity

	def addActivity(self, activity: str, time: int) -> None:
		if (not self._activities.get(activity, False)):
			self._activities[activity] = [[], 0]

		self._activities[activity][0].append(time)
		self._activities[activity][1] += time
  
		self._update(activity, self._activities[activity][1])
  
	def getTime(self, activity: str) -> int:
		return self._activities.get(activity, [[], -1])[1]

	def getTop3(self) -> List[str]:
		return self._top3



timeTracker = TimeTracker()

timeTracker.addActivity("cow", 3)
timeTracker.addActivity("horse", 4)

print(timeTracker.getTop3())			# [cow, horse]

timeTracker.addActivity("goat", 5)
timeTracker.addActivity("cow", 2)
timeTracker.addActivity("sheep", 3)

print(timeTracker.getTop3())			# [cow, horse, goat]

timeTracker.addActivity("sheep", 3)

print(timeTracker.getTop3())			# [cow, sheep, goat]

timeTracker.addActivity("horse", 1)		

print(timeTracker.getTop3())			# [cow, sheep, goat]
print(timeTracker.getTime("horse"))		# 5
print(timeTracker.getTime("rabbit"))	# -1