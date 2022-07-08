<p>Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.</p>
<p>Knowing whether a person is <code>young</code>, <code>beautiful</code> and <code>loved</code>, find out if they contradict Mary's belief.</p>
<p>A person contradicts Mary's belief if one of the following statements is true:</p>
<ul>
<li>they are <code>young</code> and <code>beautiful</code> but not <code>loved</code>;</li>
<li>they are <code>loved</code> but not <code>young</code> or not <code>beautiful</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>young = true</code>, <code>beautiful = true</code>, and <code>loved = true</code>, the output should be<br />
<code>solution(young, beautiful, loved) = false</code>.</p>
<p>Young and beautiful people are loved according to Mary's belief.</p>
</li>
<li>
<p>For <code>young = true</code>, <code>beautiful = false</code>, and <code>loved = true</code>, the output should be<br />
<code>solution(young, beautiful, loved) = true</code>.</p>
<p>Mary doesn't believe that not beautiful people can be loved.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] boolean young</strong></p>
</li>
<li>
<p><strong>[input] boolean beautiful</strong></p>
</li>
<li>
<p><strong>[input] boolean loved</strong></p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the person contradicts Mary's belief, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
