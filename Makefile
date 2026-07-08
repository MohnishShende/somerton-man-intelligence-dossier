PDF_NAME = somerton-man-assessment
MAIN = manuscript/main.tex
OUTDIR = manuscript/build
PDF_OUT = generated_output/pdf/$(PDF_NAME).pdf

.PHONY: pdf clean distclean

pdf:
	mkdir -p $(OUTDIR) generated_output/pdf
	PATH="$(CURDIR)/tools:$$PATH" latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(OUTDIR) $(MAIN)
	cp $(OUTDIR)/main.pdf $(PDF_OUT)

bootstrap-biber-macos:
	mkdir -p tools
	/usr/bin/lipo -thin arm64 /usr/local/texlive/2026/bin/universal-darwin/biber -o tools/biber-arm64
	chmod +x tools/biber-arm64
	ln -sf biber-arm64 tools/biber

clean:
	latexmk -C -outdir=$(OUTDIR) $(MAIN)
	rm -rf $(OUTDIR)

distclean: clean
	rm -f $(PDF_OUT)
