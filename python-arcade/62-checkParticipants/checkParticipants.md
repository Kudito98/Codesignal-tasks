<p>You're organizing murder mystery games for your coworkers, and came up with a lot of ideas for various groups of participants. The <code>i<sup>th</sup></code> 0-based game can be played only if there are at least <code>i</code> people registered for it. Game number <code>0</code> is a beta that you will try out with your friends, so there's no need for participants.</p>
<p>You're expecting a full house, since a lot of <code>participants</code> signed up already. Not too many, unfortunately: looks like some games can't be played, because too few people registered for them. Given the list of <code>participants</code>, your task is to return the list of games for which too few people signed up.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>participants = [0, 1, 1, 5, 4, 8]</code>, the output should be<br />
<code>solution(participants) = [2]</code>.</p>
<p>For the game number <code>2</code> (0-based) <code>2</code> people are required, but only one person has registered.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer participants</strong></p>
<p>The <code>i<sup>th</sup></code> element of the array contains the number of coworkers signed up for the <code>i<sup>th</sup></code> game.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ participants.length ≤ 100</code>,<br />
<code>0 ≤ participants[i] ≤ 150</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted array of games for which too few people signed up.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
