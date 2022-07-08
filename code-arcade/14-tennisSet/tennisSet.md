<p>In tennis, the winner of a set is based on how many games each player wins. The first player to win <code>6</code> games is declared the winner <strong>unless</strong> their opponent had already won <code>5</code> games, in which case the set continues until one of the players has won <code>7</code> games.</p>
<p>Given two integers <code>score1</code> and <code>score2</code>, your task is to determine if it is possible for a tennis set to be finished with a final score of <code>score1</code> : <code>score2</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>score1 = 3</code> and <code>score2 = 6</code>, the output should be<br />
<code>solution(score1, score2) = true</code>.</p>
<p>Since player 1 hadn't reached <code>5</code> wins, the set ends once player 2 has won <code>6</code> games.</p>
</li>
<li>
<p>For <code>score1 = 8</code> and <code>score2 = 5</code>, the output should be<br />
<code>solution(score1, score2) = false</code>.</p>
<p>Since both players won at least <code>5</code> games, the set would've ended once one of them won the <code>7<sup>th</sup></code> one.</p>
</li>
<li>
<p>For <code>score1 = 6</code> and <code>score2 = 5</code>, the output should be<br />
<code>solution(score1, score2) = false</code>.</p>
<p>This set will continue until one of these players wins their <code>7<sup>th</sup></code> game, so this can't be the final score.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer score1</strong></p>
<p>Number of games won by the <code>1<sup>st</sup></code> player, non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ score1 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer score2</strong></p>
<p>Number of games won by the <code>2<sup>nd</sup></code> player, non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ score2 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>score1 : score2</code> represents a possible score for an ended set, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
