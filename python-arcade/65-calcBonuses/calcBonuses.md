<p>You are working on a revolutionary video game. In this game the player will be able to collect several types of bonuses on each level, and his total score for the level is equal to the sum of the first <code>n</code> <code>bonuses</code> he collected. However, if he collects less than <code>n</code> bonuses, his score will be equal to <code>0</code>.</p>
<p>Given the <code>bonuses</code> the player got, your task is to return his final score for the level.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>bonuses = [4, 2, 4, 5]</code> and <code>n = 3</code>,<br />
the output should be<br />
<code>solution(bonuses, n) = 10</code>.</p>
<p><code>4 + 2 + 4 = 10</code>.</p>
</li>
<li>
<p>For <code>bonuses = [4, 2, 4, 5]</code> and <code>n = 5</code>,<br />
the output should be<br />
<code>solution(bonuses, n) = 0</code>.</p>
<p>The player has collected only <code>4</code> bonuses, so his final score is <code>0</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer bonuses</strong></p>
<p>A list of bonuses the player collected.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ bonuses.length ≤ 20</code>,<br />
<code>0 ≤ bonuses[i] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of bonuses that should be collected to obtain non-zero final score.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>Final score for the level.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
