# TARGETS

.PHONY: gs img render

# Usage: make gs n=<str>
gs:
	make render cat=gs n=${n}
	mv src/gs/gs${n}-raw.tex rendered/gs${n}/

# Usage: make render n=<str>
img:
	./utils/generate-img ${n}

# Usage: make render cat=<str> n=<str>
render:
	python utils/generate.py ${cat} ${n}
	mkdir -p rendered/${cat}${n}
	pdflatex -jobname=rendered/${cat}${n}/${cat}${n} src/${cat}/${cat}${n}.tex
	pdflatex -jobname=rendered/${cat}${n}/${cat}${n}-sol src/${cat}/${cat}${n}-sol.tex
	rm {rendered/**/*.aux,rendered/**/*.log}

clean:
	rm {src/**/gs*-sol.tex,src/**/gs*-raw.tex,src/**/gs*-img*.tex}
