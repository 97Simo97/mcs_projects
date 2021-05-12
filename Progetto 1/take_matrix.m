[N1,X1,Y1,Z1] = script_prog1("TSC_OPF_1047")

[N2,X2,Y2,Z2] = script_prog1("ns3Da")


figure(1)
semilogy(N1, X1, 'LineStyle', '--', 'Marker','square', 'Linewidth', 2, 'MarkerSize', 12, 'Color', 'b')
hold on
semilogy(N1, Y1, 'LineStyle', '--', 'Marker','x', 'Linewidth', 2, 'MarkerSize', 12, 'Color', 'r')
hold on
semilogy(N1, Z1, 'LineStyle', '--', 'Marker','x', 'Linewidth', 2, 'MarkerSize', 12, 'Color', 'y')
hold on
semilogy(N2, X2, 'LineStyle', '--', 'Marker','square', 'Linewidth', 2, 'MarkerSize', 12, 'Color', 'b')
hold on
semilogy(N2, Y2, 'LineStyle', '--', 'Marker','x', 'Linewidth', 2, 'MarkerSize', 12, 'Color', 'r')
hold on
semilogy(N2, Z2, 'LineStyle', '--', 'Marker','x', 'Linewidth', 2, 'MarkerSize', 12, 'Color', 'y')
%M = legend('\texttt{cond number}', '\texttt{error}');
%set(M, 'Interpreter', 'latex', 'FontSize', 24, 'Location','northwest');
%xlabel('\texttt{N}', 'Interpreter', 'latex', 'FontSize', 20)




