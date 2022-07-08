<p>In an effort to be more innovative, your boss introduced a strange new tradition: the first day of every month you're allowed to work from home. You like this rule when the day falls on a Monday, because any excuse to skip rush hour traffic is great!</p>
<p>You and your colleagues have started calling these months <em>regular</em> months. Since you're a fan of working from home, you decide to find out how far away the nearest <em>regular</em> month is, given that the <code>currMonth</code> has just started.</p>
<p>For your convenience, here is a list of month lengths (from January to December, respectively):</p>
<ul>
<li>Month lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
</ul>
<p>Please, note that in <a href="keyword://leap" target="_blank">leap years</a> February has <code>29</code> days.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>currMonth = "02-2016"</code>, the output should be<br />
<code>solution(currMonth) = "08-2016"</code>.</p>
<p>February of <code>2016</code> year is <em>regular</em>, but it doesn't count since it has started already, so the next <em>regular</em> month is August of <code>2016</code> - which is the answer.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string currMonth</strong></p>
<p>A string representing the current month in the format <code>mm-yyyy</code>, where <code>mm</code> is the number of the month (1-based, i.e. <code>01</code> for January, <code>02</code> for February and so on) and <code>yyyy</code> is the year.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ int(mm) ≤ 12</code>,<br />
<code>1970 ≤ int(yyyy) ≤ 2100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The earliest <em>regular</em> month after the given one in the same format as <code>currMonth</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
