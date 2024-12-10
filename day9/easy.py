#!/usr/bin/env python3

in_file = "test.txt"
in_file = "input.txt"
data = list(map(int, list(open(in_file).read().strip())))

# sum of data is length of disk
# keep two pointers, one that starts at the beginning
#   tracks position in data, position within that block, position in overall disk
#   always steps by one file block
# and one that starts at the end
#   tracks position in data, position within that block, position in overall disk
#   skips empty space
# move pointers towards each other, adding up checksum as we go
# use left pointer blocks when available, right pointer blocks when we get blanks
# when the pointers collide (try to grab data from right pointer but it is < left pointer) we're done

print(sum(data))
