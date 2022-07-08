<p>You are working on a revolutionary video game. This game will consist of several levels, and on each level the player will be able to collect bonuses. For each passed level the player will thus get some score, determined by the number of collected bonuses.</p>
<p>Player's final score is decided by the number of completed levels and scores obtained on each of them. The final score is calculated as the sum of squares of <code>n</code> maximum scores obtained. If the number of completed levels is less than <code>n</code>, the score is calculated as the sum of squared scores for each level, and final result is divided by <code>5</code> as a penalty (the result is rounded down to the nearest integer).</p>
<p>Given the list of <code>scores</code> the player got for completed levels and the number <code>n</code> that determines the number of levels you have to pass to avoid being penalized, return the player's final game score.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>scores = [4, 2, 4, 5]</code> and <code>n = 3</code>,<br />
the output should be<br />
<code>solution(scores, n) = 57</code>.</p>
<p><code>5<sup>2</sup> + 4<sup>2</sup> + 4<sup>2</sup> = 57</code>.</p>
</li>
<li>
<p>For <code>scores = [4, 2, 4, 5]</code> and <code>n = 5</code>,<br />
the output should be<br />
<code>solution(scores, n) = 12</code>.</p>
<p><code>(4<sup>2</sup> + 2<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup>) / 5 = 61 / 5 ≈ 12</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer scores</strong></p>
<p>A list of scores the player obtained.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ scores.length ≤ 20</code>,<br />
<code>0 ≤ scores[i] ≤ 50</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of levels that should be completed in order not to receive a penalty.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The final score.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
