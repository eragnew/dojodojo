from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint

url = 'http://www.codingdojo.com'
soup = BeautifulSoup(urlopen(url))

def part_one():
	link_list = []
	for elem in soup.findAll('a'):
		link_list.append(elem['href'])
	return link_list

#print part_one()

def part_two():
	link_list = part_one()
	counts = {}
	for elem in link_list:
		if elem in counts:
			counts[elem] += 1
		else:
			counts[elem] = 1
	count_set = set(val for val in counts.values())
	sorted_count_set = sorted(count_set, reverse=True)
	sorted_counts = {}
	for elem in sorted_count_set:
		sorted_counts[elem] = []
	for key, value in counts.items():
		sorted_counts[value].append(key)
	sorted_list = []
	for num in sorted_count_set:
		for elem in sorted_counts[num]:
			sorted_list.append(elem)
	return sorted_list

print part_two()






