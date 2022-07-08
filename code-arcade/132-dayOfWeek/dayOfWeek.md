<p>Whenever you decide to celebrate your birthday you always do this your favorite café, which is quite popular and as such usually very crowded. This year you got lucky: when you and your friend enter the café you're surprised to see that it's almost empty. The waiter lets slip that there are always very few people on this day of the week.</p>
<p>You enjoyed having the café all to yourself, and are now curious about the next time you'll be this lucky. Given the current <code>birthdayDate</code>, determine the number of years until it will fall on the same day of the week.</p>
<p>For your convenience, here is the list of months lengths (from January to December, respectively):</p>
<ul>
<li>Months lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
</ul>
<p>Please, note that in <a href="keyword://leap" target="_blank">leap years</a> February has <code>29</code> days. If your birthday is on the <code>29<sup>th</sup></code> of February, you celebrate it once in four years. Otherwise you birthday is celebrated each year.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>birthdayDate = "02-01-2016"</code>, the output should be<br />
<code>solution(birthdayDate) = 5</code>.</p>
<p>February 1 in <code>2016</code> is a Monday. The next year in which this same date will be Monday too is <code>2021</code>. <code>2021 - 2016 = 5</code>, which is the answer.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string birthdayDate</strong></p>
<p>A string representing the correct date in the format <code>mm-dd-yyyy</code>, where <code>mm</code> is the number of month (1-based, i.e. <code>01</code> for January, <code>02</code> for February and so on), <code>dd</code> is the day, and <code>yyyy</code> is the year.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ int(mm) ≤ 12</code>,<br />
<code>1 ≤ int(dd) ≤ 31</code>,<br />
<code>1900 ≤ int(yyyy) ≤ 2100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>An integer describing the number of years until your birthday falls on the same day of the week.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
