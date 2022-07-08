<p>Benjamin recently bought a digital clock at a magic trick shop. The seller never told Ben what was so special about it, but mentioned that one day Benjamin would be faced with a surprise.</p>
<p>Indeed, the clock did surprise Benjamin: without warning, at <code>someTime</code> the clock suddenly started going in the opposite direction! Unfortunately, Benjamin has an important meeting very soon, and knows that at <code>leavingTime</code> he should leave the house so as to not be late. Ben spent all his money on the clock, so has to figure out what time his clock will show when it's time to leave.</p>
<p>Given the <code>someTime</code> at which the clock started to go backwards, find out what time will be shown on the curious clock at <code>leavingTime</code>.</p>
<p>For your convenience, here is the list of months lengths (from January to December, respectively):</p>
<ul>
<li>Months lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
</ul>
<p>Please, note that in <a href="keyword://leap" target="_blank">leap years</a> February has <code>29</code> days.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>someTime = "2016-08-26 22:40"</code> and <code>leavingTime = "2016-08-29 10:00"</code>, the output should be<br />
<code>solution(someTime, leavingTime) = "2016-08-24 11:20"</code>.</p>
<p>There are <code>2</code> days, <code>11</code> hours and <code>20</code> minutes till the meeting. Thus, the clock will show <code>2016-08-24 11:20</code> at the <code>leavingTime</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string someTime</strong></p>
<p>The time at which the clock started going backwards. It is guaranteed that the time is correct.<br />
The time is given in the format <code>"YYYY-MM-DD HH:MM"</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1970-01-01 00:00 ≤ someTime</code>.</p>
</li>
<li>
<p><strong>[input] string leavingTime</strong></p>
<p>The time at which Ben will have to leave for the meeting in the same format as <code>someTime</code> and with the same constraints.</p>
<p><em>Guaranteed constraints:</em><br />
<code>someTime &lt; leavingTime</code>,<br />
<code>leavingTime ≤ 2035-12-31 23:59</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The time Ben's curious clock will show when it's time to leave in the same format as <code>leavingTime</code> and <code>someTime</code>. It is guaranteed that it will be not earlier than the midnight of January the 1<sup>st</sup>, 1970.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
