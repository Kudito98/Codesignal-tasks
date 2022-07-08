<p>An <em>eye rhyme</em> is a rhyme in which two words are spelled similarly but pronounced differently. An example is the pair <code>cough</code> and <code>bough</code>; although they look similar, when they are spoken there is no rhyming quality.</p>
<p>You are writing a thesis on the <em>eye rhyme</em>, and you thought it would be cool to make the text itself <em>eye rhymed</em>. This brilliant idea came to your mind a little too late: the text is already written. Now you want to check if a given pair of lines in your text have an <em>eye rhyme</em>. More specifically, you want to make sure that the last three characters of each pair of lines coincide.</p>
<p>You have already split your text into pairs of lines. Now all that's left is to check that the last three characters of the lines in each <code>pairOfLines</code> coincide. Implement a function that will do this job.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>pairOfLines = "cough\tbough"</code>, the output should be<br />
<code>solution(pairOfLines) = true</code>.</p>
<p>Both lines end with <code>ugh</code>.</p>
</li>
<li>
<p>For <code>pairOfLines = "CodeFig!ht\tWith all your might"</code>, the output should be<br />
<code>solution(pairOfLines) = false</code>.</p>
<p>The first line ends with <code>!ht</code>, and the second one ends with <code>ght</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string pairOfLines</strong></p>
<p>A string in the format <code>"&lt;line<sub>1</sub>&gt;\t&lt;line<sub>2</sub>&gt;"</code>, where <code>&lt;line<sub>i</sub>&gt;</code> consists of at least <code>3</code> characters and may contain any character except <code>'\t'</code> (tabulation character). The lines are separated by <code>'\t'</code> (tabulation character).</p>
<p><em>Guaranteed constraints:</em><br />
<code>7 ≤ pairOfLines.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the lines in <code>pairOfLines</code> have an <em>eye rhyme</em>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
