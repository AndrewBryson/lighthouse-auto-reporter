URL=your-page-url-here

lighthouse \
	--output html \
	--output json \
	--output-path="./results" \
	--chrome-flags="--headless" \
	--save-assets false \
	$URL

./process-results.py
