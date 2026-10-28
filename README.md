# Seminar 4: Supervised learning. Further insights

Open **index.html** directly in a modern browser. That single file contains the complete app, dataset generator, CSS and model code. You may copy just index.html elsewhere; no installation, server or connection is required. The app can also be hosted on GitHub Pages.

## Student workflow

1. Drag any variable into Label, or press its “Use as label” button.
2. Drag one or more other variables into Features, or use their buttons.
3. Choose random forest or logistic regression and the forest size/depth.
4. Run the model. Both classifiers are fitted on the same inputs for a fair comparison; your chosen model determines the detailed results shown.
5. Inspect accuracy, mistakes, permutation importance, cross-validation and an actual tree or regression coefficients. Switch the model selector to explore the other model without refitting.
6. Change the hypothetical profile to compare probabilities of the selected “Yes” class and the forest's individual tree estimates. Download results JSON or print to PDF to retain a run.

Every variable can be a label or a feature, but not both in the same model. For a numeric label, set a threshold: values at or above it form the Yes class; lower values form the No class. The initial midpoint is editable. Both classes need at least 10 records. Enrolled can be a binary predictor for other labels. Drag-and-drop is optional: all assignments and removals have keyboard-accessible buttons. No work is uploaded or automatically stored.

## Teaching design and honest comparison

This is a **new synthetic dataset**, not the previous executive simulation's dataset or models. It contains 1,800 fictional offer holders with six possible predictors: QS ranking, tuition, social media, interactive learning, personal tutorials and distance from home. Distance is an independent exploratory distractor. Numerical ranges and relationships are authored assumptions, not empirical findings.

The synthetic outcome is generated from alternative recruitment pathways involving thresholds and interactions, with 4% random label flips. See `data()` in model.js for the exact rule. The dataset is deliberately designed to demonstrate random forest's advantage over **main-effects logistic regression**. With all six predictors, 50 trees and depth 6, the measured fixed-split test accuracies are **95.2% versus 83.0%**. Scores are computed from predictions, not scripted or adjusted. Omitting relevant features or using shallow forests can reduce or reverse the advantage. Logistic regression with nonlinear transformations or engineered interactions is outside this exercise; the comparison does not establish a universal superiority of forests.

There is no forced root variable and no “average tree”. The tree inspector shows actual fitted trees; leaves contain observed bootstrap-sample proportions for the chosen Yes class. Forest probabilities average tree leaf probabilities.

## Methods

- Deterministic synthetic data (seed 5302), fixed stratified 70% training / 30% test split (seed 891), approximately 1,260 training and 540 test records; rounding depends on the selected label and threshold.
- Random forest: bootstrap sampling with replacement; random sqrt(p) candidate features per node; binary CART-style impurity reduction; 15 candidate quantile thresholds per candidate feature; minimum 8 records per leaf; selected depth and number of trees; fixed fitting seed 942. This is an educational approximation using quantile candidates rather than every possible split.
- Logistic regression: training-only standardisation, intercept, 1,000 full-batch gradient steps, learning rate 0.25, L2 penalty 0.002 excluding the intercept. No engineered interactions. This is a custom teaching implementation, not a validated production library.
- Classification threshold 0.5. Accuracy, precision, recall, Brier score and confusion counts are calculated from held-out predictions. Undefined precision/recall is explicitly labelled.
- Three-fold stratified CV uses the training partition only. Both models use identical folds. Scaling is fitted anew within each logistic training fold.
- Permutation importance is the mean test-accuracy decrease over three shuffles per feature. The SD reflects shuffle variation, not a confidence interval. It may be negative and does not sum to 100%. Using the test set repeatedly to select features/hyperparameters makes it less independent.
- Model settings/selections are separate from rendered results. Changes invalidate old results. Switching the detailed algorithm view uses the same fitted pair.

## Files and maintenance

`index.html` is the complete student deliverable. `page.html`, `styles.css`, `model.js`, `app.js` are maintainable source files. Run `python3 build.py` after editing them to rebuild index.html. Python is for maintainers only. No Node/npm is required for student use.

`test.cjs` checks the modelling engine (Node development-only). `browser-test.cjs` checks offline UI behaviour with Playwright (development-only). Set PLAYWRIGHT_MODULE to an installed Playwright package path if needed and CHROME_BIN to a local Chrome executable; no such libraries are included in the app. See TESTING.md.

## Limits

The page supports binary classification with any supplied variable as the label, not uploaded datasets or continuous-outcome regression. Numeric labels are converted into two classes using the student’s threshold. The demonstrated forest advantage applies to the original Enrolled target with the default settings; other targets may favour either algorithm. The forest inspector uses an expandable top-down branching outline for readability and keyboard access. Small devices use a single-column layout. There is no automatic session persistence; export results before closing. Larger forests take longer on slower hardware. Firefox, Safari and manual screen-reader testing have not yet been verified.

## GitHub Pages

Publish these files at the root of a public repository. In Settings → Pages choose Deploy from a branch, main, / (root), then Save. No build workflow is needed.
