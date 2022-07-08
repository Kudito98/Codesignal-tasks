<p>You decided to create a malicious program to play a joke on your friend. He's now struggling with a report for his work, and you want to scare him by spoiling some dates in it (of course you will change them back after you have your moment of joy). However, you don't want him to discover the errors until he starts double-checking the report, so all spoiled dates should be valid.</p>
<p>Now your goal is to write a program that modifies the <code>curDate</code> according to the rules that specify the <code>changes</code> that should be made. However, if the changes result in an incorrect date, the program should leave the date as is.</p>
<p>Given the <code>changes</code> and the <code>curDate</code>, return the spoiled date or don't change it if the result appears to be invalid.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>curDate = "01 Jul 2016 16:53:24"</code> and<br />
<code>changes = [2, 3, -1, 0, 5, 4]</code>, the output should be<br />
<code>solution(curDate, changes) = "03 Oct 2015 16:58:28"</code>;</p>
</li>
<li>
<p>For <code>curDate = "15 Mar 1998 12:09:59"</code> and<br />
<code>changes = [-2, 0, 9, 1, 3, 1]</code>, the output should be<br />
<code>solution(curDate, changes) = "15 Mar 1998 12:09:59"</code>.</p>
<p>After changing the date will look like "13 Mar 2007 13:12:60", which is incorrect, because the number of seconds cannot be equal to <code>60</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string curDate</strong></p>
<p>The current date in the format <code>"DD MMM YYYY HH:MM:SS"</code>, where <code>DD</code> stands for day of the month (1-based), <code>MMM</code> stands for the name of month cut to <code>3</code> letters (i.e. "Jan" for January, "Feb" for February and so on), <code>YYYY</code> - for the year, <code>HH</code> - for hour (your friend uses 24-hour clock), <code>MM</code> - for minutes and <code>SS</code> - for seconds. It's guaranteed that given date is correct.</p>
<p><em>Guaranteed constraints:</em><br />
<code>01 ≤ DD ≤ 31</code>,<br />
<code>MMM ∈ ["Jan", "Feb", ..., "Dec"]</code>,<br />
<code>1900 ≤ YYYY ≤ 2100</code>,<br />
<code>00 ≤ HH ≤ 23</code>,<br />
<code>00 ≤ MM ≤ 59</code>,<br />
<code>00 ≤ SS ≤ 59</code>.</p>
</li>
<li>
<p><strong>[input] array.integer changes</strong></p>
<p>An array that describes how each component of <code>curDate</code> should be updated. <code>changes[i]</code> is equal to the value that should be added to the <code>i<sup>th</sup></code> component, where <code>i</code> stands for:</p>
<ul>
<li><code>0</code>: for the day;</li>
<li><code>1</code>: for the month;</li>
<li><code>2</code>: for the year;</li>
<li><code>3</code>: for the hour;</li>
<li><code>4</code>: for the minute;</li>
<li><code>5</code>: for the second.</li>
</ul>
<p><em>Guaranteed constraints:</em><br />
<code>-30 ≤ changes[0] ≤ 30</code>,<br />
<code>-11 ≤ changes[1] ≤ 12</code>,<br />
<code>-100 ≤ changes[2] ≤ 100</code>,<br />
<code>-23 ≤ changes[3] ≤ 23</code>,<br />
<code>-59 ≤ changes[4] ≤ 59</code>,<br />
<code>-59 ≤ changes[5] ≤ 59</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The modified date if it's correct and the given date otherwise (the output should follow the same format as the input). The date is considered to be incorrect if at least one of its components is invalid.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
