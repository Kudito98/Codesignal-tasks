<p>You just bought a public transit card that allows you to ride the Metro for a certain number of days.</p>
<p>Here is how it works: upon first receiving the card, the system allocates you a <code>31</code>-day pass, which equals the number of days in January. The second time you pay for the card, your pass is extended by <code>28</code> days, i.e. the number of days in February (note that leap years are not considered), and so on. The <code>13<sup>th</sup></code> time you extend the pass, you get <code>31</code> days again.</p>
<p>You just ran out of days on the card, and unfortunately you've forgotten how many times your pass has been extended so far. However, you do remember the number of days you were able to ride the Metro during this most recent month. Figure out the number of days by which your pass will now be extended, and return all the options as an array sorted in increasing order.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>lastNumberOfDays = 30</code>, the output should be<br />
<code>solution(lastNumberOfDays) = [31]</code>.</p>
<p>There are <code>30</code> days in April, June, September and November, so the next months to consider are May, July, October or December. All of them have exactly <code>31</code> days, which means that you will definitely get a <code>31</code>-days pass the next time you extend your card.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer lastNumberOfDays</strong></p>
<p>A positive integer, the number of days for which the card was extended the last time.</p>
<p><em>Guaranteed constraints:</em><br />
<code>lastNumberOfDays = 28 or lastNumberOfDays = 30 or lastNumberOfDays = 31</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array of positive integers, the possible number of days for which you will extend your pass. The elements of the array can only be equal to <code>28</code>, <code>30</code> or <code>31</code> and must be sorted in increasing order.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
