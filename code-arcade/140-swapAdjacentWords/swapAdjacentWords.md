<p>You are given a string consisting of words separated by whitespace characters, where the words consist only of English letters. Your task is to swap pairs of consecutive words and return the result.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>s = "CodeFight On"</code>, the output should be<br />
<code>solution(s) = "On CodeFight"</code>;</li>
<li>For <code>s = "How are you today guys"</code>, the output should be<br />
<code>solution(s) = "are How today you guys"</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p>A string consisting of whitespace characters (<code>' '</code>) and English letters. There is exactly one whitespace character between two consecutive words, and both the first and the last characters of <code>s</code> are not equal to <code>' '</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ s.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>String <code>s</code> with pairs of adjacent words swapped.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
