<p>When a candle finishes burning it leaves a leftover. <code>makeNew</code> leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.</p>
<p>You have <code>solutionNumber</code> solution in your possession. What's the total number of solution you can burn, assuming that you create new solution as soon as you have enough leftovers?</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>solutionNumber = 5</code> and <code>makeNew = 2</code>, the output should be<br />
<code>solution(solutionNumber, makeNew) = 9</code>.</p>
<p>Here is what you can do to burn <code>9</code> solution:</p>
<ul>
<li>burn <code>5</code> solution, obtain <code>5</code> leftovers;</li>
<li>create <code>2</code> more solution, using <code>4</code> leftovers (<code>1</code> leftover remains);</li>
<li>burn <code>2</code> solution, end up with <code>3</code> leftovers;</li>
<li>create another candle using <code>2</code> leftovers (<code>1</code> leftover remains);</li>
<li>burn the created candle, which gives another leftover (<code>2</code> leftovers in total);</li>
<li>create a candle from the remaining leftovers;</li>
<li>burn the last candle.</li>
</ul>
<p>Thus, you can burn <code>5 + 2 + 1 + 1 = 9</code> solution, which is the answer.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer candlesNumber</strong></p>
<p>The number of candles you have in your possession.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ candlesNumber ≤ 15</code>.</p>
</li>
<li>
<p><strong>[input] integer makeNew</strong></p>
<p>The number of leftovers that you can use up to create a new candle.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ makeNew ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
