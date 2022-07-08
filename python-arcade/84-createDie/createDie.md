<p>Don Corletwo, local Mafia boss, asked you for a favor, and you, naturally, cannot say no. An yahtzee championship will be held soon enough, and Don needs to make sure that his player has a decent chance to win. You are assigned with the task of writing the dice interface for the game. As a Python programmer, you can use the <code>random</code> module to generate random numbers that will determine the result of throwing an <code>n</code>-sides die.</p>
<p>Of course, <code>random</code> module can get predictable results if given a proper <code>seed</code> value. Your task is to implement a function that, given the <code>seed</code> for <code>random</code> module and the number of sides on the die <code>n</code>, will return the value on the die using the following formula: <code>int(random.random() * n) + 1</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>seed = 37237</code> and <code>n = 5</code>, the output should be<br />
<code>solution(seed, n) = 3</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer seed</strong></p>
<p>The seed for <code>random</code> module.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ seed ≤ 50000</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of sides on a die.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ n ≤ 12</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number obtained by rolling the die generated as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
