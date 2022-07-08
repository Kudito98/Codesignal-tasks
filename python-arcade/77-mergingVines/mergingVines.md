<p>One summer Felicia was visiting her granny's summer house. There were several old and withered <code>vines</code> growing in the garden, that no longer produced grapes. Felicia found it sad, and decided to decorate the vines with wooden grapes she carved out herself. She also watered them with cola, since cola makes everything better.</p>
<p>When winter came, Felicia left, but the vines were still there, better than ever before. Each year they grew higher and wider, and the pairs of neighboring vines entangled together, forming a single vine. The wooden grapes were also doing just fine: they remained firmly attached to the vines.</p>
<p>Now that <code>n</code> years has passed, Felicia is going to visit her granny again, and she is curious about how the vines are doing. Given the number of grapes she hang on the <code>vines</code>, return the number of grapes on each vine after <code>n</code> years, assuming that each year the <code>(2 * i - 1)<sup>th</sup></code> and the <code>(2 * i)<sup>th</sup></code> vines (1-based) merged into a single vine (for each integer <code>i</code> in range <code>[1, &lt;number_of_vines&gt; / 2]</code>).</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>vines = [1, 2, 3, 4, 5]</code> and <code>n = 2</code>, the output should be<br />
<code>solution(vines, n) = [10, 5]</code>.</p>
<p>After the first year vines two pairs of vines entangled: vines <code>1</code> and <code>2</code> and vines <code>3</code> and <code>4</code> (1-based). The last vine didn't have anything to entangle with. The <code>vines</code> could thus be represented as <code>[3, 7, 5]</code>.<br />
After the second year, another pair of vines entangled. The first and the second vines entangled, forming a single vine. It's possible to represent the vines as <code>[10, 5]</code>, which is the answer.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer vines</strong></p>
<p>Array of vines, where the <code>i<sup>th</sup></code> element is the number of grapes Felicia hang on the <code>i<sup>th</sup></code> vine.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ vines.length ≤ 100</code>,<br />
<code>0 ≤ vines[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of years that have passed.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>The number of grapes on the entangled vines after <code>n</code> years.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
