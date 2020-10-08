p4: cluster.py
	cp cluster.py p4 && chmod +x p4
clean:
	rm -f p4
test:
	make && ./p4 < test.txt