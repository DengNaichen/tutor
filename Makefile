.PHONY: clean

clean:
	@echo "Cleaning up LaTeX auxiliary files..."
	@find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.synctex.gz" -o -name "*.synctex(busy)" -o -name "*.gz(busy)" \) -delete
	@echo "Done!"
